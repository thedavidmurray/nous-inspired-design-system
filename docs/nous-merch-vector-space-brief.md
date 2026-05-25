# Nous Merch — Vector Space / Calculus / LLM-as-Math Collection
## Flora Canvas Runbook | EdgelessLab Design System | 2026-05-19

---

## 1. THEME SYNTHESIS

**Core idea:** All LLMs are just high-dimensional differential equations — gradient flow through a manifold, attention as trajectory coupling, backprop as entropy dissipation. The merch should feel like scientific apparatus for observing an alien mathematical object.

**Design system anchors (mandatory per Hermes aesthetic):**
- **Courier:** Wing/helmet/staff glyphs or messenger telemetry
- **Network:** Node graph, signal path, handoff arrow, portal diagram
- **Artifact:** Halftone, scanline, riso dot, thermal print, dither, data corruption
- **Metadata:** Version stamp, route code, checksum footer, small monospace labels

**Palette (from EdgelessLab tokens):**
| Token | Hex | Role |
|-------|-----|------|
| Void Black | `#0a0a0a` | Primary background |
| Indigo | `#6366f1` | Primary accent / network lines |
| Violet | `#8b5cf6` | Secondary accent / archival wash |
| Cyan | `#06b6d4` | Tertiary accent / signal highlights |
| Green | `#22c55e` | Sparse accent / success states |
| Cream | `#f5f0e8` | Riso paper base (for print pipeline) |

---

## 2. MERCH CONCEPTS (4 Pieces)

### Piece A: "Manifold" — Poster / Hoodie Back
**Visual:** A loss landscape rendered as a bathymetric/geological cross-section. Contour lines encode gradient magnitude. Saddle points glow with cyan. Local minima are labeled with monospace version stamps. Attention heads appear as small portal glyphs embedded in the topology.

**Hermes mode:** Cyan Relay (dominant) + Mono Courier metadata
**Pipeline:** `dither-accent --accent cyan` or `riso --accent cyan`
**Prompt base (Flora-ready):**
```
Abstract topographic loss landscape, contour lines forming a mathematical manifold, saddle points glowing signal blue #133cff, gradient flow arrows as thin white lines, local minima labeled with monospace version stamps, small hexagonal portal glyphs embedded in topology, dark void black background #0a0a0a, data corruption texture at edges, Swiss grid layout, brutalist scientific visualization, not photorealistic, vector geometric style, high contrast, technical illustration aesthetic
```
**Aspect:** 4:3 (poster) or 16:9 (wide hoodie back)
**Source prompt ref:** EdgelessLab v3 CAR-02 (Geological Cross Section) + CAR-01 (Bathymetric Chart) + Hermes Cyan Relay mode

---

### Piece B: "Attention Lissajous" — T-Shirt / Sticker
**Visual:** CRT oscilloscope displaying attention-weight trajectories as Lissajous figures. Multiple overlapping ratio patterns (3:4, 5:7, 2:3) in different intensities. Phosphor persistence trails. Graticule grid with monospace timebase markers.

**Hermes mode:** Mono Courier (dominant) + Cyan accent traces
**Pipeline:** `scanline` or `dither-bw` with cyan accent layer
**Prompt base (Flora-ready):**
```
Oscilloscope CRT displaying complex Lissajous figures formed by attention weight trajectories, multiple overlapping ratio patterns 3:4 5:7 2:3 in different phosphor intensities, long persistence trails showing phase drift, graticule grid with monospace timebase markers, green and cyan phosphor glow on void black background, analog test equipment aesthetic, visible scan lines, slight barrel distortion at CRT edges, technical instrument photography, high contrast, dark laboratory background, no human figures
```
**Aspect:** 1:1 (sticker), 4:3 (chest print), 1:1 (t-shirt centered)
**Source prompt ref:** EdgelessLab v3 OSC-01 (Lissajous Figure) + OSC-04 (XY Mode Pattern) + Hermes Mono Courier mode

---

### Piece C: "Backpropagation As Entropy" — Zine Cover / Tote Bag
**Visual:** Ordered crystalline structure on left gradually dissolving into random particle distribution on right. The phase boundary is a gradient descent trajectory. Information decay as halftone dot dissolution. Thermal print banding artifacts across the composition.

**Hermes mode:** Violet Archive (dominant) + Riso Broadcast broadcast dots
**Pipeline:** `thermal` or `riso --accent violet`
**Prompt base (Flora-ready):**
```
Abstract entropy gradient visualization, ordered crystalline tensor structure on left gradually dissolving into random particle distribution on right, phase transition boundary marked by gradient descent trajectory line, information decay shown through halftone dot dissolution, thermal print banding artifacts across composition, violet archival ink wash #4d4ca8, risograph dot texture on cream paper base #f5f0e8, small monospace metadata stamps at boundary points, dark background left transitioning to warm paper right, thermodynamic aesthetic, scientific illustration, not photorealistic, dithered texture throughout
```
**Aspect:** 16:9 (zine cover), 3:4 (tote bag vertical), 1:1 (tote square)
**Source prompt ref:** EdgelessLab v3 DEC-08 (Entropy Gradient) + Hermes Violet Archive mode

---

### Piece D: "Token Constellation" — Poster / Sticker Sheet
**Visual:** High-dimensional vector space projected as stellar cartography. Each point is a token embedding. Constellation lines connect semantically related tokens. Distance = cosine similarity. A central "sun" is the [CLS] token. Survey grid coordinates in monospace.

**Hermes mode:** Cyan Relay (dominant) + Violet Archive halftone wash
**Pipeline:** `dither-full` (keeps all accent colors) or `riso` multi-color
**Prompt base (Flora-ready):**
```
Stellar cartography of a high-dimensional vector space, hundreds of small glowing points representing token embeddings, constellation lines connecting semantically related tokens in signal blue #133cff, distance encoding cosine similarity as line thickness, central bright sun representing CLS token, survey grid coordinates in monospace font, deep void black space background #0a0a0a, violet halftone wash in empty regions, small registration marks and checksum footer in corners, astronomical survey aesthetic, Swiss grid precision, dark technical illustration, not photorealistic, vector geometric style
```
**Aspect:** 1:1 (poster), 4:3 (sticker sheet backing card)
**Source prompt ref:** EdgelessLab v3 CAR-10 (Tectonic Plate Map adapted to embedding space) + NAV-06 (Celestial Navigation) + Hermes Cyan Relay mode

---

## 3. MODEL COMPARISON MATRIX (Flora Canvas)

Run each of the 4 prompts through these 5 models on Flora canvas. The goal is to understand how each model handles: structural precision, dark-field rendering, text/label legibility, texture detail, and color accuracy against the Edgeless palette.

| Model | Flora Cost | Strength | Weakness to Watch |
|-------|-----------|--------|-------------------|
| **Flux 2 Pro** | 6-94 credits | Structure, dark fields, prompt adherence | May smooth dither textures |
| **Ideogram 3.0** | 80 credits | **Text/label legibility** (best for metadata stamps) | Can oversaturate dark palette |
| **Recraft V4 Pro** | 54-320 credits | **Vector/SVG output** → plotter-ready merch | Style may deviate from gritty aesthetic |
| **GPT Image 2** | 50-178 credits | Nuanced detail, atmospheric depth | Expensive, may "prettify" the brutalist vibe |
| **Seedream 4.5** | 40-54 credits | Vivid color, fast | Less control on precise geometry |

**Recommended workflow:**
1. Start with Flux 2 Pro for each prompt (fast, establishes baseline)
2. Run Ideogram 3.0 for pieces with heavy metadata/text (A and D)
3. Run Recraft V4 Pro for pieces destined for physical plotter or vector merch (all)
4. Run GPT Image 2 for the hero poster (highest detail budget)
5. Seedream 4.5 as a wildcard/color test

**Scoring rubric (per EDGA-701 pattern):**
| Dimension | Weight | What to score |
|-----------|--------|---------------|
| Dark-field fidelity | 20% | Does `#0a0a0a` stay black or get lifted to gray? |
| Structural precision | 20% | Are grid lines straight? Are Lissajous ratios correct? |
| Text legibility | 20% | Can you read the monospace stamps at 50% scale? |
| Texture authenticity | 20% | Does dither/scanline/thermal look real or AI-smooth? |
| Color accuracy | 20% | Do cyan/violet/indigo match Edgeless tokens? |

---

## 4. FLORA CANVAS EXECUTION GUIDE

Since Flora API requires technique slugs (no discovery endpoint), use the Flora web canvas:

1. Open https://flora-fauna.ai/canvas
2. New canvas → Add Image Generation node
3. Paste prompt from above
4. Set model (dropdown)
5. Aspect ratio per piece
6. Generate. If first attempt loses the gritty texture, add: `--style raw` or append "gritty, structural dithering, not smooth gradients, dark brutalist"
7. Download PNG immediately (URLs are temporary)
8. Save to `generated/nous-merch-flora-<model>-<piece>/`

**Post-processing (after Flora output):**
```bash
# For print-ready merch:
python3.11 /Users/djm/claude-projects/products/edgelesslab-design-system/scripts/edgeless-texture-pipeline.py \
  input.png --mode dither-accent --accent cyan -o output.png

# For riso simulation:
python3.11 .../edgeless-texture-pipeline.py input.png --mode riso --accent violet -o output.png

# For thermal/receipt aesthetic:
python3.11 .../edgeless-texture-pipeline.py input.png --mode thermal -o output.png
```

---

## 5. MERCH ITEM MAPPING

| Piece | Primary Item | Secondary | Pipeline | Target Size |
|-------|-------------|-----------|----------|-------------|
| A: Manifold | Hoodie back print | A2 poster | `dither-accent --accent cyan` | 16:9 |
| B: Attention Lissajous | T-shirt front | Sticker (die-cut) | `scanline` or `dither-bw` | 1:1 |
| C: Backprop As Entropy | Tote bag | Zine cover | `thermal` or `riso --accent violet` | 3:4 |
| D: Token Constellation | A3 poster | Sticker sheet | `dither-full` (multi-color) | 1:1 |

---

## 6. NEXT STEPS

1. **Run Flora canvas** for all 4 prompts × 5 models = 20 generations
2. **Score** against rubric, save to `_meta/merch-scores.csv`
3. **Post-process** top 2-3 per piece through Edgeless texture pipeline
4. **Plotter test:** Run Recraft V4 SVG outputs through `pen-plotter-art/scripts/nous-color-split.py` for physical A3 plot proof
5. **Production:** Export final PNGs at 300 DPI for DTG/sticker printing

---

*Generated by Hive#2662 | EdgelessLab Design System v3 | Flora Canvas Runbook*
