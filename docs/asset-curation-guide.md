# Asset Curation Guide

Reference for turning Midjourney output into curated design system assets.

---

## Workflow

### 1. Generate in Midjourney

Run prompts from `prompts/all-prompts-v2.txt` with:

```
--style raw --stylize 100-350 --v 6.1
```

Select **upscaled singles** (U1-U4), never raw grids. Pick the variant with the strongest structural composition.

### 2. Process through the texture pipeline

```bash
python3.11 scripts/edgeless-texture-pipeline.py input.png \
  --mode <mode> \
  --accent <color> \
  -o public/processed/<category>/<category>-<number>-<mode>.png
```

Available modes: `dither-bw`, `dither-accent`, `dither-full`, `riso`, `scanline`, `thermal`

Accent colors (for `dither-accent` and `riso`): `cyan`, `violet`, `indigo`, `green`, `white`

### 3. Naming convention

```
{category}-{number}-{mode}.png
```

Examples:
- `env-01-dither-bw.png`
- `diag-03-dither-accent-cyan.png`
- `edit-07-thermal.png`

### 4. Storage

All processed assets go in `public/processed/{category}/`.

---

## Pipeline Mode Recommendations by Category

| Category | Primary Mode | Secondary Mode |
|----------|-------------|----------------|
| Environments | `scanline` | `dither-bw` |
| Diagrams | `dither-accent cyan` | `dither-bw` |
| Editorial | `thermal` | `riso violet` |
| Textures | `dither-bw` | `dither-full` |
| Cosmic | `scanline` | `dither-accent indigo` |
| Artifacts | `thermal` | `dither-bw` |
| Archive | `thermal` | `dither-bw`, `riso violet` |
| UI Screens | `scanline` | `dither-accent cyan` |
| Surveillance | `dither-bw` | `dither-accent cyan` |
| Infrastructure | `dither-bw` | `dither-accent cyan` |
| Cartography | `riso` | `dither-accent` |
| Biology | `dither-full` | `dither-bw` |
| Audio | `dither-accent cyan` | `scanline` |
| Typography | `dither-bw` | `thermal` |
| Ritual | `dither-full` | `dither-accent indigo` |

---

## Quality Criteria

An asset is ready for the design system when it meets all of these:

- **No human faces or figures.** Abstract, structural, mechanical subjects only.
- **Strong structural composition.** Clear focal point, intentional negative space, readable at a glance.
- **Works at multiple sizes.** Must hold up from 64px thumbnail to full-width hero. Test both.
- **Dithering enhances the subject.** The post-processing should add texture and character, not turn the image into noise. If the subject is unrecognizable after processing, choose a different mode or a different source image.
- **Consistent with the palette.** Void black (`#0a0a0a`) backgrounds, white foreground elements, accent colors from the canonical palette (indigo, violet, cyan, green). No off-palette colors leaking through.

---

## Batch Processing

Process an entire category directory at once:

```bash
python3.11 scripts/edgeless-texture-pipeline.py \
  --batch downloads/environments/ \
  --mode dither-bw \
  --output-dir public/processed/environments/
```

To generate both recommended modes for a category:

```bash
# Environments: scanline + dither-bw
python3.11 scripts/edgeless-texture-pipeline.py \
  --batch downloads/environments/ \
  --mode scanline \
  --output-dir public/processed/environments/

python3.11 scripts/edgeless-texture-pipeline.py \
  --batch downloads/environments/ \
  --mode dither-bw \
  --output-dir public/processed/environments/
```

For accent modes, specify the color:

```bash
python3.11 scripts/edgeless-texture-pipeline.py \
  --batch downloads/diagrams/ \
  --mode dither-accent \
  --accent cyan \
  --output-dir public/processed/diagrams/
```
