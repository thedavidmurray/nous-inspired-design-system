# Nous Girl reference images

Source: NOUS RESEARCH OFFICIAL BRANDING BOOKLET, First Edition (Feb 5 2024), produced by John Galt.

These are the canonical mascot references for use as Midjourney `--cref` (character reference), the MJ alpha web "Image Prompts" panel, ImageMagick post-render overlay, or any other character-consistency tool.

| File | Source | Notes |
|---|---|---|
| `nous-girl-ref-A-large-portrait.png` | Brand-book p.9, large left sketch | Preferred primary reference. 3/4 view, full bust, headphone band visible, bob cut + bangs |
| `nous-girl-ref-B-spiral.png` | Brand-book p.9, top-right sketch | 3/4 view, spiral-bound sketchbook page edge |
| `nous-girl-ref-C-eyes-down.png` | Brand-book p.9, middle-right sketch | Looking down / eyes closed, blouse visible |
| `nous-girl-ref-D-back-three-quarter.png` | Brand-book p.9, bottom-right sketch | 3/4 view from behind, neck and headphones visible |
| `nous-girl-ref-E-source-mascot.png` | Brand-book front cover / page 2 | The badge-style portrait used as the main brand mascot |

## When to use

- **MJ `--cref` (recommended)**: drag one of these into the MJ alpha web app's *Image Prompts* panel before submitting a batch; ~70% character consistency across the batch
- **Compositing**: pair with the `overlay-nous-girl.sh` and `add-nous-wordmark.sh` scripts in `generated/nous-girl-overlay/` to layer her as a silhouette + wordmark onto rendered backgrounds
- **Style training**: viable training inputs for a future LoRA or character profile if MJ's cref drift becomes unworkable

## Do not modify

These are the original brand-book extractions. Crop / recolor / restyle versions should live in a sibling directory (e.g. `nous-girl-derived/`) and link back to the source file used.
