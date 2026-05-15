#!/usr/bin/env python3
"""
Edgeless Lab Texture Pipeline
Applies structural dithering and print-simulation effects to match
the aesthetic of physical originals (dot-matrix, thermal, risograph).
"""

import argparse
import math
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

# ---------------------------------------------------------------------------
# Canonical Edgeless palette
# ---------------------------------------------------------------------------
PALETTE = {
    "void":    (10, 10, 10),
    "indigo":  (99, 102, 241),
    "violet":  (139, 92, 246),
    "cyan":    (6, 182, 212),
    "white":   (255, 255, 255),
    "green":   (34, 197, 94),
}

ACCENT_ALIASES = {
    "indigo": "indigo",
    "violet": "violet",
    "cyan":   "cyan",
    "green":  "green",
    "white":  "white",
}

# 8x8 Bayer threshold matrix (normalised to 0-63, we scale at use-time)
BAYER_8x8 = [
    [ 0, 48, 12, 60,  3, 51, 15, 63],
    [32, 16, 44, 28, 35, 19, 47, 31],
    [ 8, 56,  4, 52, 11, 59,  7, 55],
    [40, 24, 36, 20, 43, 27, 39, 23],
    [ 2, 50, 14, 62,  1, 49, 13, 61],
    [34, 18, 46, 30, 33, 17, 45, 29],
    [10, 58,  6, 54,  9, 57,  5, 53],
    [42, 26, 38, 22, 41, 25, 37, 21],
]


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def clamp(v, lo=0, hi=255):
    return max(lo, min(hi, int(v)))


def color_distance_sq(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1, c2))


def nearest_palette_color(pixel, palette):
    """Return the palette colour closest to pixel (Euclidean RGB)."""
    return min(palette, key=lambda c: color_distance_sq(pixel, c))


def luminance(r, g, b):
    return 0.299 * r + 0.587 * g + 0.114 * b


# ---------------------------------------------------------------------------
# MODE: dither-bw  (1-bit Floyd-Steinberg via PIL)
# ---------------------------------------------------------------------------

def mode_dither_bw(img):
    grey = img.convert("L")
    bw = grey.convert("1")  # PIL Floyd-Steinberg dithering
    return bw.convert("RGB")


# ---------------------------------------------------------------------------
# MODE: dither-accent  (ordered Bayer dither to void + one accent)
# ---------------------------------------------------------------------------

def mode_dither_accent(img, accent_name="cyan"):
    accent = PALETTE.get(accent_name, PALETTE["cyan"])
    void = PALETTE["void"]

    grey = img.convert("L")
    w, h = grey.size
    pixels_in = grey.load()
    out = Image.new("RGB", (w, h))
    pixels_out = out.load()

    for y in range(h):
        for x in range(w):
            lum = pixels_in[x, y]  # 0-255
            # Bayer threshold scaled to 0-255
            threshold = (BAYER_8x8[y % 8][x % 8] / 63.0) * 255
            if lum > threshold:
                pixels_out[x, y] = accent
            else:
                pixels_out[x, y] = void

    return out


# ---------------------------------------------------------------------------
# MODE: dither-full  (Floyd-Steinberg error diffusion to full 5-colour palette)
# ---------------------------------------------------------------------------

def mode_dither_full(img):
    palette_colors = [
        PALETTE["void"],
        PALETTE["indigo"],
        PALETTE["violet"],
        PALETTE["cyan"],
        PALETTE["white"],
    ]

    img = img.convert("RGB")
    w, h = img.size

    # Work with float buffer for error diffusion
    buf = [list(img.getpixel((x, y)) for x in range(w)) for y in range(h)]

    out = Image.new("RGB", (w, h))
    pixels_out = out.load()

    for y in range(h):
        for x in range(w):
            old = buf[y][x]
            new = nearest_palette_color(old, palette_colors)
            pixels_out[x, y] = new

            err = tuple(o - n for o, n in zip(old, new))

            # Floyd-Steinberg diffusion weights
            for dx, dy, w_frac in [(1, 0, 7/16), (-1, 1, 3/16), (0, 1, 5/16), (1, 1, 1/16)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h:
                    prev = buf[ny][nx]
                    buf[ny][nx] = tuple(clamp(prev[c] + err[c] * w_frac) for c in range(3))

    return out


# ---------------------------------------------------------------------------
# MODE: riso  (risograph halftone simulation)
# ---------------------------------------------------------------------------

def make_halftone_channel(grey_img, dot_spacing, angle_deg, color):
    """
    Create a halftone separation for one colour channel.
    Each cell of the grid gets a filled circle whose radius is proportional
    to the darkness of the source at that cell centre.
    """
    w, h = grey_img.size
    pixels = grey_img.load()

    # We render at 1x — the dot grid IS the pixel grid at dot_spacing intervals
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(out)

    cos_a = math.cos(math.radians(angle_deg))
    sin_a = math.sin(math.radians(angle_deg))

    half = dot_spacing / 2.0
    max_r = half * 0.95  # max dot radius

    # Walk a rotated grid that covers the whole image
    diag = math.sqrt(w * w + h * h)
    steps = int(diag / dot_spacing) + 2

    for gy in range(-steps, steps):
        for gx in range(-steps, steps):
            # Grid position (rotated)
            cx = gx * dot_spacing
            cy = gy * dot_spacing
            # Rotate into image space (centred on image middle)
            ix = int(cos_a * cx - sin_a * cy + w / 2)
            iy = int(sin_a * cx + cos_a * cy + h / 2)

            if ix < 0 or ix >= w or iy < 0 or iy >= h:
                continue

            lum = pixels[ix, iy]
            darkness = 1.0 - (lum / 255.0)
            r = max_r * math.sqrt(darkness)  # sqrt keeps area proportional

            if r < 0.5:
                continue

            draw.ellipse(
                [ix - r, iy - r, ix + r, iy + r],
                fill=(*color, 220),  # slight transparency for overlap blending
            )

    return out


def mode_riso(img, accent_name="cyan"):
    accent = PALETTE.get(accent_name, PALETTE["cyan"])
    # Two-channel riso: void/black ink + accent ink
    # Cream paper base (#f5f0e8)
    cream = (245, 240, 232)

    img = img.convert("RGB")
    w, h = img.size

    grey = img.convert("L")

    dot_spacing = 6  # pixels between dot centres

    # Black channel: driven by overall darkness
    black_halftone = make_halftone_channel(grey, dot_spacing, 45, PALETTE["void"])

    # Accent channel: driven by inverted luminance (shadows get more accent)
    # Shift the curve so midtones get the most accent
    accent_grey = grey.point(lambda p: clamp(int(255 - abs(p - 100) * 2.0)))
    accent_halftone = make_halftone_channel(accent_grey, dot_spacing, 15, accent)

    # Composite: cream base, then accent, then black on top
    paper = Image.new("RGB", (w, h), cream)
    paper.paste(accent_halftone, (0, 0), accent_halftone)
    paper.paste(black_halftone, (0, 0), black_halftone)

    return paper.convert("RGB")


# ---------------------------------------------------------------------------
# MODE: scanline  (CRT / VHS simulation)
# ---------------------------------------------------------------------------

def mode_scanline(img):
    img = img.convert("RGB")
    w, h = img.size
    pixels = img.load()

    out = Image.new("RGB", (w, h))
    pixels_out = out.load()

    for y in range(h):
        # Reduce bit depth: quantise each channel to 5 bits (32 levels)
        # Every other scanline is darkened
        scanline_dim = 0.55 if (y % 3 == 0) else 1.0

        # Horizontal glitch offset: every ~30 lines, shift by a few pixels
        h_offset = 0
        if y % 37 < 2:
            h_offset = (y * 7) % 5 - 2  # -2 to +2 pixel shift

        for x in range(w):
            sx = (x + h_offset) % w
            r, g, b = pixels[sx, y]

            # Quantise to 32 levels then scale back
            r = (r >> 3) << 3
            g = (g >> 3) << 3
            b = (b >> 3) << 3

            # Apply scanline darkening
            r = clamp(int(r * scanline_dim))
            g = clamp(int(g * scanline_dim))
            b = clamp(int(b * scanline_dim))

            pixels_out[x, y] = (r, g, b)

    # Slight phosphor bloom: very mild blur on bright areas only
    return out


# ---------------------------------------------------------------------------
# MODE: thermal  (thermal printer simulation)
# ---------------------------------------------------------------------------

def mode_thermal(img):
    img = img.convert("L")
    w, h = img.size

    # High contrast curve: crush midtones
    contrast_lut = []
    for i in range(256):
        # Sigmoid-like contrast boost
        v = i / 255.0
        v = 1.0 / (1.0 + math.exp(-12 * (v - 0.45)))
        contrast_lut.append(clamp(int(v * 255)))

    img = img.point(contrast_lut)

    # Apply Floyd-Steinberg dither to 1-bit for that thermal dot feel
    bw = img.convert("1")
    img = bw.convert("L")
    pixels = img.load()

    out = Image.new("L", (w, h))
    pixels_out = out.load()

    for y in range(h):
        # Thermal horizontal banding: random-ish intensity variation per line
        band_factor = 1.0
        if y % 7 == 0:
            band_factor = 0.85
        elif y % 11 == 0:
            band_factor = 0.92

        for x in range(w):
            v = pixels[x, y]
            v = clamp(int(v * band_factor))
            pixels_out[x, y] = v

    out_rgb = out.convert("RGB")

    # Very slight horizontal blur to mimic thermal head smear
    # PIL requires square odd-sized kernels, so use 3x3 with horizontal bias
    out_rgb = out_rgb.filter(ImageFilter.Kernel(
        size=(3, 3),
        kernel=[0, 0, 0,
                1, 2, 1,
                0, 0, 0],
        scale=4,
        offset=0,
    ))

    return out_rgb


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

MODES = {
    "dither-bw":     mode_dither_bw,
    "dither-accent": None,  # needs accent arg
    "dither-full":   mode_dither_full,
    "riso":          None,  # needs accent arg
    "scanline":      mode_scanline,
    "thermal":       mode_thermal,
}

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff"}


def process_image(input_path, mode, accent, output_path):
    img = Image.open(input_path).convert("RGB")
    print(f"  [{mode}] {input_path} ({img.size[0]}x{img.size[1]})")

    if mode == "dither-accent":
        result = mode_dither_accent(img, accent)
    elif mode == "riso":
        result = mode_riso(img, accent)
    else:
        result = MODES[mode](img)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    result.save(output_path)
    print(f"  -> {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Edgeless Lab texture pipeline — structural dithering & print simulation"
    )
    parser.add_argument("input", nargs="?", help="Input image path")
    parser.add_argument("--mode", required=True, choices=list(MODES.keys()),
                        help="Processing mode")
    parser.add_argument("--accent", default="cyan", choices=list(ACCENT_ALIASES.keys()),
                        help="Accent colour (for dither-accent and riso modes)")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--batch", help="Process all images in this directory")
    parser.add_argument("--output-dir", help="Output directory for batch mode")

    args = parser.parse_args()

    if args.batch:
        if not args.output_dir:
            print("Error: --output-dir required with --batch", file=sys.stderr)
            sys.exit(1)

        batch_dir = Path(args.batch)
        if not batch_dir.is_dir():
            print(f"Error: {batch_dir} is not a directory", file=sys.stderr)
            sys.exit(1)

        files = sorted(f for f in batch_dir.iterdir() if f.suffix.lower() in IMAGE_EXTS)
        if not files:
            print(f"No image files found in {batch_dir}", file=sys.stderr)
            sys.exit(1)

        print(f"Batch processing {len(files)} images with mode={args.mode}")
        for f in files:
            out_name = f"{f.stem}-{args.mode}{f.suffix}"
            out_path = str(Path(args.output_dir) / out_name)
            process_image(str(f), args.mode, args.accent, out_path)

        print(f"Done. {len(files)} images processed.")

    else:
        if not args.input:
            print("Error: input image path required (or use --batch)", file=sys.stderr)
            sys.exit(1)

        if not os.path.isfile(args.input):
            print(f"Error: {args.input} not found", file=sys.stderr)
            sys.exit(1)

        output = args.output or f"{Path(args.input).stem}-{args.mode}.png"
        process_image(args.input, args.mode, args.accent, output)
        print("Done.")


if __name__ == "__main__":
    main()
