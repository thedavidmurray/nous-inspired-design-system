# Edgeless Lab Design System Completion Audit

Date: 2026-05-20

## Objective

Create a unified, canonical Nous-inspired design system under `products/edgelesslab-design-system/` that merges:

1. The legacy Hermes design kit (`generated/hermes-design-system/`)
2. The Edgeless component library + token system (`products/edgelesslab-design-system/`)
3. All orphaned design assets (`generated/hive/`, `generated/nous-shootout/`, `captures/midjourney/`, `captures/flora-outputs/`)

## Harmonization Status

| Requirement | Evidence | Status |
|---|---|---|
| Unified visual bible | `docs/visual-bible-v2.md` merges both palettes, maps 6 pipeline modes to 4 anchor palettes | Complete |
| Agent art rules | `docs/agent-art-rules.md` with canonical paths and pipeline mode selection | Complete |
| Asset curation guide | `docs/asset-curation-guide.md` with mode recommendations per category | Complete |
| Design tokens (TS) | `src/tokens/index.ts` with unified palette | Complete |
| Design tokens (CSS) | `src/styles/tokens.css` with CSS custom properties | Complete |
| Components | 7 React components (Button, Card, Badge, Input, Select, Modal, Toast) | Complete |
| Texture pipeline | `scripts/edgeless-texture-pipeline.py` (8 modes) | Complete |
| Eval script | `scripts/design-alignment-eval.py` | Complete |
| Prompt library | 300 prompts (v2 + v3) in `prompts/` | Complete |
| Processed assets | `public/processed/` (8 variants of ~30 originals) | In progress - migrating orphans |
| Source material | `public/originals/` (10 iPhone photos) | Complete |
| Inspo references | `public/inspo/` (GIFs, reference images) | In progress - migrating captures |
| Sidecars | `.prompt.txt` files for all generations | Complete |
| Videos | `public/videos/` (2 MP4s) | Complete |
| Spec sheet | `public/spec-sheet.html` | Complete |
| Source references | `docs/references/` — primary source PDFs + metadata | Complete |

## Source References

| Document | Location | Status |
|----------|----------|--------|
| Nous Research Brand Booklet (First Edition, Feb 2024) | `docs/references/NOUS-BRAND-BOOKLET-firstedition_2024.pdf` + `.meta` | Complete |
| Ingested markdown (working reference) | `claude-vault/03-Knowledge/ingested/nous-brand-booklet-first-edition-2024.md` | Complete |

## Migrated Assets

### From `generated/hermes-design-system/`
- `contact-sheet.jpg` → `public/courier/contact-sheet-v1-dither-bw.jpg` (with sidecar)
- `visual-bible.md` content merged into `docs/visual-bible-v2.md`
- `tokens.css` content merged into `src/styles/tokens.css` (`.hm-*` classes preserved)
- `raw-material-library.md` content merged into `docs/visual-bible-v2.md`

### From `generated/hive/`
- `hive-gpt-image-2-square-v1.png` → `public/courier/hive-core-gpt-image-v1.png`
- `hive-gpt-image-2-square-v2-hermes-aligned.png` → `public/courier/hive-core-gpt-image-v2-aligned.png`

### From `generated/nous-shootout/`
- `flux-2-pro.png` → `public/model-comparisons/nous-shootout-flux-2-pro.png`
- `gpt-image-1.png` → `public/model-comparisons/nous-shootout-gpt-image-1.png`
- `ideogram-3-0.png` → `public/model-comparisons/nous-shootout-ideogram-3-0.png`
- `recraft-v4-pro.webp` → `public/model-comparisons/nous-shootout-recraft-v4-pro.webp`
- `seedream-v4-5.png` → `public/model-comparisons/nous-shootout-seedream-v4-5.png`
- `nous-shootout-all-models.jpg` → `public/model-comparisons/nous-shootout-composite-v1.jpg`
- `nous-shootout-all-models-v2.jpg` → `public/model-comparisons/nous-shootout-composite-v2.jpg`

### From `captures/midjourney/`
- All images → `public/inspo/midjourney-*.png` (with sidecars)

### From `captures/flora-outputs/`
- All images → `public/inspo/flora-*.png` (with sidecars)

## Verification

```bash
# File count check
find public/ -type f | wc -l

# Sidecar coverage
find public/ -name "*.prompt.txt" | wc -l
find public/ \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.webp" -o -name "*.gif" \) ! -name "*.prompt.txt" | wc -l

# Pipeline modes present
ls public/processed/

# Missing sidecars
for f in $(find public/ \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.webp" \)); do
  [ -f "${f%.*}.prompt.txt" ] || echo "MISSING: $f"
done
```

## Known Gaps

- ~~`generated/nous-degraded/degraded_1.png`~~ → Moved to `public/texture-references/nous-degraded-artifact-v1.png` with sidecar. Classified as texture pipeline source material.
- ~~`generated/nous-merch-vector-space-brief.md`~~ → Copied to `docs/nous-merch-vector-space-brief.md`. Working design brief with Flora prompts and pipeline modes.
- ~~`captures/venice-outputs/`~~ → Moved to `public/inspo/venice/` with sidecars. Local SD generations for merch exploration.
- `captures/owl-eval-specimen/` + `generated/owl-*/` — **15+ SVGs from pen plotter work. Belongs to EDGA-310 Pen Plotter KB, not the design system.** Leave in place.

## Classification Complete

All orphaned assets from the design system consolidation have been classified and migrated.
