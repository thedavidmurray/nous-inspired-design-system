# Edgeless Lab Design System

Dark-first component library, design tokens, and texture pipeline for the Edgeless Lab visual identity. Structural dithering, not smooth gradients.

Open `public/spec-sheet.html` locally for a visual preview of the full system.

## Quick Start

### For Developers (React / Tailwind)

```bash
pnpm add @edgelesslab/design-system
```

```tsx
import { Button, Card, Badge } from '@edgelesslab/design-system';
import '@edgelesslab/design-system/styles';
```

Add the Tailwind preset to your `tailwind.config.ts`:

```ts
import edgelessPreset from '@edgelesslab/design-system/tailwind';

export default {
  presets: [edgelessPreset],
  content: [/* your paths */],
};
```

See [Components](#components) below for the full list with status.

### For Designers (Tokens + Assets)

Tokens ship in two formats -- use whichever fits your toolchain:

| Format | File | Works with |
|--------|------|------------|
| TypeScript | `src/tokens/index.ts` | Direct import, Style Dictionary input |
| CSS Custom Properties | `src/styles/tokens.css` | Any project -- drop in and use `var(--color-accent-primary)` |

The CSS file is self-contained: fonts, colors, typography, spacing, radius, shadows, motion, z-index. Dark theme is the default; add `data-theme="light"` to opt into light mode.

Typography: **JetBrains Mono** for display, headings, code, and labels. **Inter** for body text.

Processed assets live in `public/processed/{category}/`. See `docs/asset-curation-guide.md` for the full curation workflow.

### For Content Creators (Prompt Library + Pipeline)

300 prompts across 30 categories, split into two complementary sets:

| Set | File | Categories | Target |
|-----|------|------------|--------|
| v2 | `prompts/all-prompts-v2.txt` | 15 (Environments, Diagrams, Editorial, Textures, Cosmic, Artifacts, Archive, UI Screens, Surveillance, Infrastructure, Cartography, Biology, Audio, Typography, Ritual) | Midjourney v6.1: `--style raw --stylize 100-350 --v 6.1` |
| v3 | `prompts/all-prompts-v3.txt` | 15 (Oscilloscope, Metallurgy, Cartographic-Deep, Printmaking, Mechanical, Optics, Textile, Chemistry, Navigation, Transmission, Measurement, Decay, Notation, Computation, Containment) | Midjourney v8.1 |

Workflow: pick a prompt, generate in Midjourney/Flux/etc, then post-process:

```bash
python3.11 scripts/edgeless-texture-pipeline.py input.png --mode dither-bw -o output.png
```

Batch an entire directory:

```bash
python3.11 scripts/edgeless-texture-pipeline.py --batch images/ --mode riso --accent cyan --output-dir processed/
```

See [Pipeline Modes](#pipeline-modes) and `docs/asset-curation-guide.md` for mode recommendations per category.

## Palette

| Token | Hex | Use |
|-------|-----|-----|
| Void Black | `#0a0a0a` | Primary background |
| White | `#ffffff` | Primary foreground |
| Indigo | `#6366f1` | Primary accent |
| Violet | `#8b5cf6` | Secondary accent |
| Cyan | `#06b6d4` | Tertiary accent |
| Green | `#22c55e` | Success / sparse accent |
| Cream | `#f5f0e8` | Riso paper base |

## Components

| Component | Export | Status |
|-----------|--------|--------|
| Button | `Button`, `ButtonProps` | Done |
| Card | `Card`, `CardProps` | Done |
| Badge | `Badge`, `BadgeProps` | Done |
| Input | `Input`, `InputProps` | Done |
| Select | `Select`, `SelectProps` | Done |
| Modal | `Modal`, `ModalProps`, `ModalFooter` | Done |
| Toast | `Toast`, `ToastProps`, `ToastContainer` | Done |

All components are React/TSX with Tailwind classes. Import individually or from the barrel:

```tsx
import { Button, Card, Badge, Input, Select, Modal, Toast } from '@edgelesslab/design-system';
```

## Prompt Categories

| v2 (150 prompts, MJ v6.1) | v3 (150 prompts, MJ v8.1) |
|---|---|
| Environments (12) | Oscilloscope (10) |
| Diagrams (12) | Metallurgy (10) |
| Editorial (12) | Cartographic-Deep (10) |
| Textures (10) | Printmaking (10) |
| Cosmic (10) | Mechanical (10) |
| Artifacts (10) | Optics (10) |
| Archive (8) | Textile (10) |
| UI Screens (10) | Chemistry (10) |
| Surveillance (10) | Navigation (10) |
| Infrastructure (10) | Transmission (10) |
| Cartography (8) | Measurement (10) |
| Biology (8) | Decay (10) |
| Audio (8) | Notation (10) |
| Typography (8) | Computation (10) |
| Ritual (8) | Containment (10) |

## Project Structure

```
src/
  components/          React components (Button, Card, Badge, Input, Select, Modal, Toast)
  tokens/              Design token definitions (TypeScript)
  styles/              CSS custom properties (tokens.css) + global styles
  tailwind-preset.ts   Tailwind preset wiring tokens into your config

prompts/
  all-prompts-v2.txt   150 prompts, 15 categories (MJ v6.1)
  all-prompts-v3.txt   150 prompts, 15 categories (MJ v8.1)

scripts/
  edgeless-texture-pipeline.py   Post-processing pipeline (Pillow only)
  design-alignment-eval.py       Rubric-based eval scorer

public/
  originals/           Nous-sourced reference photographs (ground truth)
  inspo/               Aesthetic reference images and GIFs
  processed/           Pipeline output, organized by category
  spec-sheet.html      Visual spec sheet (open locally)

docs/
  asset-curation-guide.md   Full curation workflow with mode recommendations
```

## Pipeline Modes

| Mode | Algorithm | Aesthetic |
|------|-----------|-----------|
| `dither-bw` | Floyd-Steinberg 1-bit | Dot-matrix, high contrast B&W |
| `dither-accent` | Bayer 8x8 ordered | Two-color cross-hatch pattern |
| `dither-full` | Floyd-Steinberg 5-color | Full palette error diffusion |
| `riso` | Halftone dot screen | Risograph print on cream paper |
| `thermal` | Sigmoid + F-S dither | Receipt printer with banding |
| `scanline` | CRT simulation | Scanline darkening + glitch |

Accent colors for `dither-accent` and `riso`: `--accent cyan|violet|indigo|green|white`

## Eval

Score assets against the design tokens rubric:

```bash
python3.11 scripts/design-alignment-eval.py --all
```

## Requirements

- **Node 18+** with **pnpm** -- components and Tailwind preset
- **Python 3.11+** with **Pillow** -- texture pipeline and eval

## License

MIT
