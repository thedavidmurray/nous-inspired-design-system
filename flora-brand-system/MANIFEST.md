# Edgeless Brand System — Flora generative library

Reproducible spec for the Edgeless Lab brand-asset library built on Flora.
This is the reusable source of truth: prompts, model routing, and structure —
not just the flattened output. Re-run or extend from here.

- **Flora project:** `prj_ns78jxd7nz0hhgw1ebww313ea58e23dt` (workspace `ws_qd752sph6h4ghbj0swpa9mj9gd7w8n7d`)
- **Canvas:** https://app.flora.ai/projects/ns78jxd7nz0hhgw1ebww313ea58e23dt
- **Built:** 2026-09-08 · grounded in `edgelesslab.com/DESIGN.md` (canonical visual system)

## Two visual languages (from DESIGN.md)
- **Field Sheet** (editorial / Field Notes / plotter / print): Paper `#f3eddd`, Ink `#0c0a08`, ONE natural-pigment accent per project — malachite `#1a6847`, sodium amber `#c2410c` (plotter), woad blue `#2d4a7a` (Tartanism), oxide `#c96846` (editions/Shop). Riso/toner specimen plates, crop marks, hairline rules, foxing.
- **Night Lab** (site / product / systems): Night `#09090b`, Carbon `#111113`, Signal lime `#c6f24e` (live state only), Relay blue `#7aa2ff` (routing focus only). Terminal/captured-artifact panels, hairline dividers, square corners.
- Type in production overlay (NOT baked by the model): Boska display, Geist Sans UI, JetBrains Mono metadata.

## Model → workflow routing (from Flora YouTube learnings)
| Workflow | Model | Note |
|---|---|---|
| Field Sheet specimens (subject-heavy) | **Flux 2 Max** (`t2i-flux-2-max`, ~0.055/img) | subject-forward prompt; renders full content + legible headers |
| Wide/cheap exploration | Flux 2 Klein 4B (`t2i-flux-2-klein-4b`, ~0.004) | roll wide, promote winners to Max |
| Night Lab system captures | Flux 2 Pro / GPT Image | dark-field fidelity |
| Real captions / typographic plates | Ideogram 3.0 / Recraft V4 | only these set legible text |
| Glyphs / marks → plotter SVG | Recraft V4 Vector / Arrow 1.1 Max, or `Anything to Vector` technique (`tech_ts742h62cgfgbgf7f53kjxqp558b0aaa`) | clean vector paths |
| Product / Shop / LineFields mockups | Nano Banana Pro + `PDP Set` (`tech_ts78c60r4cb6d3r0h8czaddt4d8avbvx`) | product realism |
| UGC / group people | Nano Banana Pro | best realistic group photos |
| Char-consistent illustration (Monsters Moved In) | reference-driven consistency + i2i chaining | HELD |
| Post-process (dither/riso/accent) | `edgeless-texture-pipeline.py` (offline) | bakes on-brand texture |

## PROMPT DISCIPLINE (the fix)
- **Subject-forward:** lead with the specimen; say it "FILLS most of the plate"; end negatives with "NOT a blank or empty plate." (Over-weighting "empty reserved bands" produced empty tiles on weak models.)
- Reference-anchor loop for coherence: take a strong hit → free `Prompt Extractor` (`tech_ts779wsqasrt2w92f70zaj3hs584y39d`) → reuse the extracted look on new subjects with the anchor attached.
- Real captions/headers are typeset later in the production overlay, not generated.

## Family / motif structure (12 families; Field Sheet content set proven on Flux 2 Max)
FS_INK (no accent): recursive branching tree · moire interference field · circle-packing · flow-field streamlines
FS_BOTANICAL (malachite): fern vascular · leaf venation · root-system spread · seed-head dispersal
FS_PLOTTER (amber): harmonograph trace · concentric interference basin · spirograph loops · machine cross-hatch
FS_TARTAN (woad): sett grid · thread lattice · twill diagonal · check overlay
FS_SERIAL (malachite): twelve-tone matrix · rhythmic notation grid · pitch-class wheel · permutation table
FS_EDITION (oxide): stacked print edge · deckled-edge print · material swatch grid · deboss mark
FS_GLYPH (ink+accent): isolated mark · mark-in-brackets · cropped mark · mark-in-cell → SVG lane
FS_SUBSTRATE (neutral): paper-fiber · toner-grain · riso-noise · blank hairline frame (reusable material)
NL_QUEUE · NL_VIZ · NL_PANEL · NL_STATUS (Night Lab; validated on cheap model, re-run on Flux 2 Pro for finals)

## Naming: `EL_<FAM>_M<motif>_<MODEL>` → `__APPROVED` / `__HERO_800` / `__SVG`

## Reusable (promote), not flattened:
- **Elements:** approved isolated specimens, clean substrate fields, SVG glyphs, blank composition frames, artwork-faithful product-mockup bases.
- **Techniques to save:** Field-Sheet plate finisher, Night-Lab framing, ink-only glyph→SVG extraction, Shop PDP derivation, hero/category/thumbnail resizing.
- Do NOT promote baked-in fake text, or specimens with permanently baked rules/captions (those go in the production overlay).

## Generator
The combinatorial fan-out (axes × values × subject-forward templates, fired via the Flora `execute` TS loop) is the reusable engine. Small batches (≤8/call) avoid code-runner timeouts. See session log / re-request the generator to extend.
