# Edgeless Lab Visual Bible v2
# Unified Nous-Inspired Design Language

## Position

Edgeless Lab is the visual system for a working agent network: mythic courier, technical lab, print artifact, and corrupted transmission. It should feel operational before it feels decorative. Every surface should look like it was printed, scanned, routed through a noisy network, and recovered with intent.

## Core Principles

1. Ink before light. Start from flat ink, paper, toner, cyanotype, or risograph. Add glow only when it represents signal, portal, or telemetry.
2. Motifs carry meaning. Wings mean movement, helmets mean proxy identity, staffs mean routing, lines mean agent relationships, portals mean tool access.
3. Glitch is structural. Use tears, barcode gaps, scanlines, and pixel debris as containers, separators, or state indicators. Do not sprinkle noise randomly.
4. Editorial density over generic minimalism. Compositions can be quiet, but they should still include registration marks, metadata, labels, or diagram traces.
5. One dominant reproduction mode per artifact. Cyanotype, risograph green, black photocopy, or violet scan should not all compete in the same surface.
6. Grit must survive production. The system should still work when printed, thresholded, screenshotted, compressed, or used by another agent without the original references.

## Four Anchors

Every artifact needs all four anchors:

- Courier: wing, helmet, staff, messenger, relay, or route language.
- Network: agent graph, handoff line, signal path, portal, queue, or telemetry.
- Artifact: halftone, scanline, riso, cyanotype, photocopy, thermal print, bitmap, or corruption.
- Metadata: version, route, date, agent, checksum, status, footer label, or small operational caption.

If an output feels weak, check the anchors first. Most failures are missing metadata or using texture without a routing idea.

## Mode System: Pipeline Modes vs Anchor Palettes

The design system operates on two layers:

| Pipeline Mode | Accent | Anchor Palette | Primary Use |
|---|---|---|---|
| dither-bw | none (1-bit) | Mono Courier | Docs, proofs, command surfaces, high-legibility UI |
| dither-accent-cyan | cyan (#06b6d4) | Cyan Relay | Research, systems maps, dashboard hero moments, network state |
| dither-accent-violet | violet (#8b5cf6) | Violet Archive | Datasets, model cards, memory pages, historical artifacts |
| dither-full | full palette | Mixed / Contextual | Full-color error diffusion when all accents needed |
| riso-cyan | cyan (#06b6d4) | Cyan Relay | Social images, event posters, zines, calls for participation |
| riso-violet | violet (#8b5cf6) | Violet Archive | Archive prints, dataset provenance, model cards |
| thermal | thermal gradient | Mono Courier | Receipt-style artifacts, operational logs, telemetry strips |
| scanline | none (CRT) | Cyan Relay | Monitor-like surfaces, technical overlays, live system views |

### Anchor Palette Definitions

#### Mono Courier
- Pipeline: dither-bw, thermal
- Tokens: void-black #0a0a0a background, white #ffffff foreground, carbon #050505 ink
- Texture: bitmap stipple, photocopy grain, dashed frame rules, toner grit
- Type: heavy condensed labels plus readable monospace body
- Motifs: agent graph, courier marks, small metadata strips

#### Cyan Relay
- Pipeline: dither-accent-cyan, riso-cyan, scanline
- Tokens: cyan #06b6d4 accent, indigo #6366f1 secondary, signal-blue #133cff electric
- Texture: scanlines, overexposed halos, technical overlays
- Type: uppercase labels, small coordinate readouts
- Motifs: portals, arrows, eye/observer crops, line networks

#### Violet Archive
- Pipeline: dither-accent-violet, riso-violet
- Tokens: violet #8b5cf6 accent, lavender #aeb9ff wash, blueprint #061f59 deep field
- Texture: halftone wash, horizontal corruption bars, low-fidelity scan
- Type: dataset labels, archival captions, restrained headings
- Motifs: helmets, statues, masks, fragmentary anatomy

#### Riso Broadcast
- Pipeline: riso-cyan or riso-violet (social contexts)
- Tokens: riso-green #178c58 ink, cream #f5f0e8 paper base, carbon #050505 text
- Texture: riso misregistration, dot screens, overprint blocks
- Type: large slab or compressed display type with small sponsor/footer row
- Motifs: repeated figures, badges, stamp icons, tiled symbols

## Unified Token Palette

| Token | Hex | Role | Anchor |
|---|---|---|---|
| void-black | #0a0a0a | Deepest background | All |
| carbon | #050505 | Primary ink | Mono Courier |
| white | #ffffff | Primary foreground | All |
| indigo | #6366f1 | Primary accent | Cyan Relay |
| violet | #8b5cf6 | Secondary accent | Violet Archive |
| cyan | #06b6d4 | Tertiary accent | Cyan Relay |
| signal-blue | #133cff | Electric network blue | Cyan Relay |
| riso-green | #178c58 | Broadcast ink | Riso Broadcast |
| cream | #f5f0e8 | Riso paper base | Riso Broadcast |
| lavender | #aeb9ff | Pale scan wash | Violet Archive |
| blueprint | #061f59 | Deep cyanotype field | Cyan Relay |
| green | #22c55e | Success / sparse accent | Semantic |
| warning | #f59e0b | Amber status | Semantic |
| error | #ef4444 | Red alert | Semantic |

## Typography Direction

Use installed system fonts first, then swap in licensed fonts later.

- Display: condensed impact typography. Use JetBrains Mono for display/headings, or Impact / Arial Black / Druk / Compacta / Obviously Condensed for poster work.
- Technical labels: IBM Plex Mono, SFMono-Regular, Menlo, ui-monospace, JetBrains Mono.
- Body: Inter for product UI, Georgia for editorial notes. Keep body type quiet.
- Rules: uppercase labels, tight line-height for posters, generous line-height for documentation, no negative letter spacing.

## Texture Rules

- Halftone: use dot fields for image translation and surface depth. Prefer small black or white dots over soft gradients.
- Scanline: use horizontal interference only on technical or monitor-like surfaces.
- Pixel debris: use square fragments at edges, under captions, or as state markers.
- Registration marks: use corner ticks, crop marks, dashed borders, tiny metadata and date stamps.
- Corruption bars: use as meaningful dividers, selected states, or asset provenance strips.
- Hard shadows: prefer print-offset shadows over soft shadows.
- Damage bands: one severe tear is better than low-opacity noise everywhere.

## Composition Rules

- Prefer tall portrait posters, square social tiles, and dense dashboard panels.
- Crop faces aggressively: eyes, helmets, or silhouette profiles can dominate.
- Put metadata at the bottom or right edge, not as centered explanatory text.
- Use thick frames sparingly. A frame should imply print, portal, or captured screen.
- Use line networks as structure behind content, not as decorative spaghetti.

## Icon And Motif Language

- Wing: speed, relay, outbound action.
- Helmet: agent identity, proxy, runtime.
- Staff/caduceus: routing, orchestration, protected exchange.
- Portal: tool access, model gateway, handoff between systems.
- Eye: observation, evaluation, audit.
- Node figure: human or agent in the swarm.
- Arrow: directed handoff, queue movement, chain of custody.
- Barcode strip: corrupted payload, data transfer, artifact boundary.

## Forbidden Moves

- No purple-blue SaaS gradient heroes.
- No glassmorphism, soft cards, or cheerful rounded pill overload.
- No generic "AI network" glowing blobs.
- No random ancient Greek clip art without print or systems treatment.
- No decorative glitch that harms legibility.
- No one-note dark blue interface where every element is the same hue.
- No long explanatory copy inside the artifact itself.
- No polished cyberpunk chrome, lens flares, smooth neon tubes, or raytraced icons.
- No agent outputs that invent new palettes without adding them back to tokens.css.

## Usage Matrix

| Surface | Mode | Notes |
|---|---|---|
| Paperclip issue art | Mono Courier or Violet Archive | Prioritize text legibility and issue metadata. |
| Agent dashboard | Cyan Relay | Let network lines represent actual routing or state. |
| Social event poster | Riso Broadcast | Use bold display type, footer metadata, limited palette. |
| Model/dataset card | Violet Archive | Use artifact naming, checksums, version stamps. |
| Internal docs | Mono Courier | Clean body type, high contrast, sparse texture. |
| Component library | Mono Courier + Cyan accents | Keep UI functional, texture supports hierarchy. |

## Image Generation Recipes

Use these as prompt modules. Combine one subject module, one reproduction module, one composition module, and one constraint module.

### Subject Modules

- Mythic courier agent: "a Hermes-like messenger figure as an autonomous software agent, winged helmet reduced to graphic silhouette, caduceus converted into routing hardware, no literal brand logos"
- Agent network portrait: "anonymous agents represented as small human glyphs connected by white routing lines, dense but readable graph topology, operational control-room feeling"
- Research portal: "overexposed circular portal above a human face crop, technical map overlays, sparse coordinate labels, blueprint scan atmosphere"
- Dataset helmet: "ancient messenger helmet rendered as a corrupted dataset artifact, halftone scan, horizontal error strip, small archival label"
- Broadcast tile: "repeated anime editorial figures holding identical signal objects, riso overprint, large cropped display type, small footer metadata"

### Reproduction Modules

- "black and white photocopy, hard threshold, bitmap stipple, uneven toner, no gray gradients"
- "Prussian blue cyanotype, white signal lines, scanline interference, overexposed highlights"
- "green risograph on warm cream paper, misregistration, ink gain, halftone fill"
- "violet-blue archival scan, halftone wash, corrupted horizontal transfer bar"
- "thermal printer artifact, low-resolution bitmap, OCR debris, dashed crop frame"

### Composition Modules

- "portrait poster, one dominant face crop, footer metadata strip, dashed outer crop border"
- "square social tile, centered symbol, heavy icon field, sparse side labels"
- "wide dashboard header, agent graph in the background, dense status panels in foreground"
- "specimen sheet, four modes arranged as print tests, tiny provenance labels"
- "zine page, asymmetric type, overprinted stamp icons, visible registration marks"

### Constraint Modules

- "limited to two inks and paper stock"
- "no glossy 3D, no smooth vector gradients, no generic sci-fi UI"
- "text areas left blank or filled only with simple metadata labels"
- "must survive monochrome thresholding"
- "emphasize print grain and diagram structure over painterly detail"

## Poster Layout Recipes

### Office Hours

- Square or 4:5.
- One large mythic figure or helmet crop.
- Three-line uppercase event title set at a slight rotation.
- Footer: date, channel, small agent mark.
- Reproduction: cyanotype or mono photocopy.

### Dataset Drop

- Square.
- Artifact image centered with left label.
- One corruption strip across lower third.
- Footer checksum/date/version.
- Reproduction: violet archive.

### Network Broadcast

- Wide or square.
- Agent graph fills the surface.
- Small glyph nodes, thin routing lines.
- No long title. Let the topology be the message.
- Reproduction: signal blue and white.

## Agent-Network Diagram Recipes

- Nodes are people-shaped glyphs or square agents, not circles by default.
- Lines must show direction through arrows, thickness, or broken handoff segments.
- Use one hub only when the real system has a hub. Otherwise use messy federation.
- Include metadata: agent, route, latency, status, handoff.
- Keep 20-40 percent empty space so the graph can breathe.

## Post-Processing Recipes

Use ImageMagick or the built-in pipeline:

```bash
# ImageMagick standalone
magick input.png -colorspace Gray -ordered-dither o8x8,6 -contrast-stretch 2%x2% output-halftone.png
magick input.png -colors 2 -type bilevel output-threshold.png
magick input.png -modulate 100,0 -fill "#061f59" -colorize 80 output-blueprint.png

# Edgeless pipeline (canonical)
python3.11 scripts/edgeless-texture-pipeline.py input.png --mode dither-bw -o output.png
python3.11 scripts/edgeless-texture-pipeline.py --batch images/ --mode riso --accent cyan --output-dir processed/
```

For UI textures:

1. Generate or select a high-contrast source.
2. Convert to grayscale.
3. Apply threshold or ordered dither.
4. Crop to a tileable or edge-framed region.
5. Export as PNG/WebP under an asset folder.
6. Use CSS mix-blend-mode: multiply or screen only when legibility survives.

## CSS Texture Primitives

```css
.hm-halftone {
  background-image: radial-gradient(currentColor 1px, transparent 1.2px);
  background-size: 7px 7px;
}

.hm-scanline {
  background-image: repeating-linear-gradient(
    to bottom,
    rgba(255,255,255,.18) 0 1px,
    transparent 1px 5px
  );
}

.hm-corrupt-strip {
  height: 14px;
  color: currentColor;
  background:
    linear-gradient(90deg, currentColor 0 11%, transparent 11% 14%, currentColor 14% 29%, transparent 29% 34%, currentColor 34% 49%, transparent 49% 53%, currentColor 53% 71%, transparent 71% 76%, currentColor 76% 100%);
}

.hm-pixel-debris {
  background-image: conic-gradient(from 90deg, currentColor 25%, transparent 0 50%, currentColor 0 75%, transparent 0);
  background-size: 10px 10px;
}

.hm-toner-grit {
  background-image:
    radial-gradient(currentColor .8px, transparent 1px),
    radial-gradient(currentColor .55px, transparent .8px),
    repeating-linear-gradient(0deg, transparent 0 5px, currentColor 5px 6px);
  background-position: 0 0, 9px 13px, 0 0;
  background-size: 18px 22px, 27px 31px, auto;
  opacity: .14;
  mix-blend-mode: multiply;
  pointer-events: none;
}
```

## Sources & References

| Document | Location | Role |
|----------|----------|------|
| Nous Research Brand Booklet (First Edition, Feb 2024) | `docs/references/NOUS-BRAND-BOOKLET-firstedition_2024.pdf` + `.meta` | Primary source of truth for Nous typography, color, and manifesto language |
| Ingested markdown (working reference) | `claude-vault/03-Knowledge/ingested/nous-brand-booklet-first-edition-2024.md` | Searchable, annotated extraction of the PDF |

The Nous brand booklet is the foundational document from which the Edgeless Lab system emerged. It should be consulted when making decisions about type hierarchy, color anchoring, or editorial voice. Our system extends and adapts the booklet's vision rather than replicating it.
