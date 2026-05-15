#!/usr/bin/env python3
"""
Edgeless Lab — Showcase Video Generator
Creates aesthetic showcase videos from processed pipeline images.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# Canonical palette
VOID = (10, 10, 10)
CYAN = (6, 182, 212)
VIOLET = (139, 92, 246)
WHITE = (255, 255, 255)
GREY = (255, 255, 255, 100)

CANVAS_W, CANVAS_H = 1080, 1080  # Square for social
FPS = 30

ROOT = Path(__file__).parent.parent
PROCESSED = ROOT / "public" / "processed"
ORIGINALS = ROOT / "public" / "originals"
GEN_V2 = ROOT / "public" / "generatedExamples" / "v2"
OUTPUT = ROOT / "public" / "videos"


def get_font(size):
    """Try to load JetBrains Mono or fall back to Menlo/Courier."""
    for name in [
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Courier.dfont",
        "/Library/Fonts/JetBrainsMono-Bold.ttf",
    ]:
        if os.path.exists(name):
            try:
                return ImageFont.truetype(name, size)
            except Exception:
                continue
    return ImageFont.load_default()


def make_frame(img_path, label_top, label_bottom, canvas_size=(CANVAS_W, CANVAS_H)):
    """Create a branded frame from an image with labels."""
    canvas = Image.new("RGB", canvas_size, VOID)
    draw = ImageDraw.Draw(canvas)

    # Load and fit image
    img = Image.open(img_path).convert("RGB")
    iw, ih = img.size

    # Leave room for labels: 80px top, 60px bottom
    avail_w = canvas_size[0] - 40  # 20px padding each side
    avail_h = canvas_size[1] - 140  # 80 top + 60 bottom

    scale = min(avail_w / iw, avail_h / ih)
    new_w = int(iw * scale)
    new_h = int(ih * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)

    # Center in available area
    x = (canvas_size[0] - new_w) // 2
    y = 80 + (avail_h - new_h) // 2
    canvas.paste(img, (x, y))

    # Top label
    font_top = get_font(28)
    draw.text((20, 20), label_top, fill=CYAN, font=font_top)

    # Bottom label
    font_bot = get_font(16)
    draw.text((20, canvas_size[1] - 50), label_bottom, fill=WHITE, font=font_bot)

    # Accent line under top label
    draw.rectangle([20, 55, 200, 57], fill=CYAN)

    return canvas


def make_transition_frames(frame_a, frame_b, n_frames=15):
    """Generate crossfade transition frames between two images."""
    frames = []
    for i in range(n_frames):
        alpha = i / (n_frames - 1)
        blended = Image.blend(frame_a, frame_b, alpha)
        frames.append(blended)
    return frames


def frames_to_video(frames_dir, output_path, fps=FPS):
    """Assemble numbered frames into an MP4."""
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(fps),
        "-i", str(frames_dir / "frame_%05d.png"),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", "18",
        "-preset", "slow",
        str(output_path),
    ]
    subprocess.run(cmd, check=True, capture_output=True)


# =========================================================================
# VIDEO 1: MODE MORPH — cycle one image through all 8 pipeline modes
# =========================================================================
def make_mode_morph():
    print("=== VIDEO 1: MODE MORPH ===")

    # Pick the best source images for morphing
    sources = [
        ("courier-relay-orbital", "COURIER RELAY"),
        ("v2-01b-hive-core-styleref-8154", "HIVE CORE"),
        ("v2-02b-kilo-chamber-styleref-8163", "KILO CHAMBER"),
    ]

    modes = [
        ("dither-bw", "DITHER-BW // Floyd-Steinberg 1-bit"),
        ("dither-accent-cyan", "DITHER-ACCENT // Bayer 8x8 + Cyan"),
        ("dither-accent-violet", "DITHER-ACCENT // Bayer 8x8 + Violet"),
        ("dither-full", "DITHER-FULL // 5-Color Error Diffusion"),
        ("riso-cyan", "RISO // Halftone Dot Screen + Cyan"),
        ("riso-violet", "RISO // Halftone Dot Screen + Violet"),
        ("thermal", "THERMAL // Receipt Printer Sim"),
        ("scanline", "SCANLINE // CRT Monitor Sim"),
    ]

    frames_dir = OUTPUT / "_frames_morph"
    if frames_dir.exists():
        shutil.rmtree(frames_dir)
    frames_dir.mkdir(parents=True)

    frame_idx = 0
    hold_frames = 45  # 1.5 sec hold on each mode
    transition_frames = 12  # 0.4 sec crossfade

    for src_name, src_label in sources:
        # Build frames for each mode
        mode_images = []
        for mode_dir, mode_label in modes:
            img_path = PROCESSED / mode_dir / f"{src_name}.png"
            if not img_path.exists():
                print(f"  Skipping {img_path} (not found)")
                continue
            frame = make_frame(
                img_path,
                f"EDGELESS LAB // {src_label}",
                f"{mode_label}   |   NOUS INSPIRED DESIGN SYSTEM",
            )
            mode_images.append(frame)

        if not mode_images:
            continue

        # Hold + transition between each mode
        for i, frame in enumerate(mode_images):
            # Hold
            for _ in range(hold_frames):
                frame.save(frames_dir / f"frame_{frame_idx:05d}.png")
                frame_idx += 1

            # Crossfade to next (or loop back to first)
            if i < len(mode_images) - 1:
                next_frame = mode_images[i + 1]
            else:
                next_frame = mode_images[0]

            for tf in make_transition_frames(frame, next_frame, transition_frames):
                tf.save(frames_dir / f"frame_{frame_idx:05d}.png")
                frame_idx += 1

        # Brief black separator between sources
        black = Image.new("RGB", (CANVAS_W, CANVAS_H), VOID)
        draw = ImageDraw.Draw(black)
        font = get_font(20)
        draw.text((CANVAS_W // 2 - 60, CANVAS_H // 2 - 10), "EDGELESS", fill=CYAN, font=font)
        for _ in range(20):
            black.save(frames_dir / f"frame_{frame_idx:05d}.png")
            frame_idx += 1

    print(f"  {frame_idx} frames generated")

    output_path = OUTPUT / "edgeless-mode-morph.mp4"
    frames_to_video(frames_dir, output_path)
    shutil.rmtree(frames_dir)
    print(f"  -> {output_path}")
    return output_path


# =========================================================================
# VIDEO 2: GALLERY REEL — quick-cut montage of best processed images
# =========================================================================
def make_gallery_reel():
    print("=== VIDEO 2: GALLERY REEL ===")

    # Curated selection of best processed images across modes
    gallery = [
        # (mode_dir, filename, label)
        ("dither-bw", "IMG_8154-dither-bw.jpg", "IMG_8154 // DITHER-BW"),
        ("dither-accent-cyan", "IMG_8154-dither-accent.jpg", "IMG_8154 // ACCENT CYAN"),
        ("riso-cyan", "IMG_8155-riso.jpg", "IMG_8155 // RISO CYAN"),
        ("dither-full", "IMG_8155-dither-full.jpg", "IMG_8155 // DITHER-FULL"),
        ("thermal", "IMG_8156-thermal.jpg", "IMG_8156 // THERMAL"),
        ("dither-bw", "IMG_8157-dither-bw.jpg", "IMG_8157 // DITHER-BW"),
        ("scanline", "IMG_8163-scanline.jpg", "IMG_8163 // SCANLINE"),
        ("dither-accent-violet", "IMG_8160-dither-accent.jpg", "IMG_8160 // ACCENT VIOLET"),
        ("riso-violet", "IMG_8159-riso.jpg", "IMG_8159 // RISO VIOLET"),
        ("dither-bw", "courier-relay-orbital.png", "COURIER RELAY // DITHER-BW"),
        ("dither-full", "courier-relay-orbital.png", "COURIER RELAY // DITHER-FULL"),
        ("riso-cyan", "courier-relay-orbital.png", "COURIER RELAY // RISO CYAN"),
        ("thermal", "courier-relay-orbital.png", "COURIER RELAY // THERMAL"),
        ("dither-bw", "v2-01b-hive-core-styleref-8154.png", "HIVE CORE // DITHER-BW"),
        ("dither-accent-cyan", "v2-01b-hive-core-styleref-8154.png", "HIVE CORE // ACCENT CYAN"),
        ("thermal", "v2-02b-kilo-chamber-styleref-8163.png", "KILO CHAMBER // THERMAL"),
        ("dither-full", "v2-04-editorial-cover-ideogram.png", "EDITORIAL // DITHER-FULL"),
        ("riso-violet", "v2-04-editorial-cover-ideogram.png", "EDITORIAL // RISO VIOLET"),
        ("dither-bw", "IMG_8161-dither-bw.jpg", "IMG_8161 // DITHER-BW"),
        ("dither-full", "IMG_8162-dither-full.jpg", "IMG_8162 // DITHER-FULL"),
        ("thermal", "IMG_8158-thermal.jpg", "IMG_8158 // THERMAL"),
        ("scanline", "IMG_8159-scanline.jpg", "IMG_8159 // SCANLINE"),
        ("dither-bw", "bluedither-dither-bw.png", "INSPO DITHER // DITHER-BW"),
        ("dither-full", "liminalspace-dither-full.png", "LIMINAL // DITHER-FULL"),
        ("thermal", "liminalspace-thermal.png", "LIMINAL // THERMAL"),
    ]

    frames_dir = OUTPUT / "_frames_reel"
    if frames_dir.exists():
        shutil.rmtree(frames_dir)
    frames_dir.mkdir(parents=True)

    frame_idx = 0
    hold_frames = 24  # 0.8 sec per image (quick cuts)
    transition_frames = 6  # 0.2 sec fast crossfade

    valid_frames = []
    for mode_dir, filename, label in gallery:
        img_path = PROCESSED / mode_dir / filename
        if not img_path.exists():
            print(f"  Skipping {img_path}")
            continue
        frame = make_frame(
            img_path,
            "EDGELESS LAB",
            f"{label}   |   NOUS INSPIRED DESIGN SYSTEM",
        )
        valid_frames.append(frame)

    # Opening title card
    title = Image.new("RGB", (CANVAS_W, CANVAS_H), VOID)
    draw = ImageDraw.Draw(title)
    font_big = get_font(48)
    font_sub = get_font(18)
    font_sm = get_font(14)
    draw.text((CANVAS_W // 2 - 200, CANVAS_H // 2 - 80), "EDGELESS", fill=WHITE, font=font_big)
    draw.text((CANVAS_W // 2 - 50, CANVAS_H // 2 - 20), "LAB", fill=CYAN, font=font_big)
    draw.rectangle([CANVAS_W // 2 - 200, CANVAS_H // 2 + 40, CANVAS_W // 2 + 200, CANVAS_H // 2 + 42], fill=CYAN)
    draw.text((CANVAS_W // 2 - 180, CANVAS_H // 2 + 55), "NOUS INSPIRED DESIGN SYSTEM", fill=WHITE, font=font_sub)
    draw.text((CANVAS_W // 2 - 120, CANVAS_H // 2 + 85), "TEXTURE PIPELINE v2.0", fill=(255, 255, 255, 128), font=font_sm)

    # Hold title
    for _ in range(60):  # 2 sec
        title.save(frames_dir / f"frame_{frame_idx:05d}.png")
        frame_idx += 1

    prev_frame = title
    for frame in valid_frames:
        # Transition
        for tf in make_transition_frames(prev_frame, frame, transition_frames):
            tf.save(frames_dir / f"frame_{frame_idx:05d}.png")
            frame_idx += 1
        # Hold
        for _ in range(hold_frames):
            frame.save(frames_dir / f"frame_{frame_idx:05d}.png")
            frame_idx += 1
        prev_frame = frame

    # End card
    end = Image.new("RGB", (CANVAS_W, CANVAS_H), VOID)
    draw = ImageDraw.Draw(end)
    draw.text((CANVAS_W // 2 - 200, CANVAS_H // 2 - 40), "EDGELESS", fill=WHITE, font=font_big)
    draw.text((CANVAS_W // 2 - 50, CANVAS_H // 2 + 20), "LAB", fill=CYAN, font=font_big)

    for tf in make_transition_frames(prev_frame, end, 20):
        tf.save(frames_dir / f"frame_{frame_idx:05d}.png")
        frame_idx += 1
    for _ in range(45):
        end.save(frames_dir / f"frame_{frame_idx:05d}.png")
        frame_idx += 1

    print(f"  {frame_idx} frames generated ({len(valid_frames)} images)")

    output_path = OUTPUT / "edgeless-gallery-reel.mp4"
    frames_to_video(frames_dir, output_path)
    shutil.rmtree(frames_dir)
    print(f"  -> {output_path}")
    return output_path


if __name__ == "__main__":
    OUTPUT.mkdir(parents=True, exist_ok=True)
    v1 = make_mode_morph()
    v2 = make_gallery_reel()
    print(f"\nDone. Videos at:\n  {v1}\n  {v2}")
