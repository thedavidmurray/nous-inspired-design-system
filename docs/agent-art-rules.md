# Agent Art Rules

## Required Reading Order

1. `docs/visual-bible-v2.md` for the unified design grammar.
2. `src/styles/tokens.css` for implementation primitives.
3. `docs/asset-curation-guide.md` for the full curation workflow.
4. `scripts/design-alignment-eval.py` for verification.

## Working Rule

Every Edgeless artifact must include all four anchors:

- Courier: wing, helmet, staff, messenger, relay, or route language.
- Network: agent graph, handoff line, signal path, portal, queue, or telemetry.
- Artifact: halftone, scanline, riso, cyanotype, photocopy, thermal print, bitmap, or data corruption.
- Metadata: version, route, date, agent, checksum, status, or small footer labels.

If one anchor is missing, revise before handing off.

## Mode Selection

Pick one dominant pipeline mode per artifact:

- dither-bw / thermal: docs, command surfaces, issue art, proof sheets.
- dither-accent-cyan / riso-cyan / scanline: dashboards, network maps, live system views, social posts.
- dither-accent-violet / riso-violet: datasets, model cards, memory artifacts, provenance pages.

Do not mix all modes in one asset. A secondary accent is allowed only for metadata or state.

## Implementation Rules

- Import `src/styles/tokens.css` first.
- Use existing `.hm-*` classes before adding new primitives.
- Add new tokens only when they will be reused by at least two surfaces.
- Keep cards square or tightly rounded. Avoid soft SaaS panels.
- Texture must support hierarchy or state. Do not add noise as decoration only.
- Preserve text legibility at mobile widths.

## Image Generation Rules

- Use `docs/visual-bible-v2.md` prompt modules.
- Never copy a source reference directly.
- Generate at least three variants per target: one faithful, one more severe/gritty, one more restrained/product-safe.
- Save generated assets with mode, subject, model/tool, date, and seed when available.

Example naming:

```text
cyan-relay_agent-network_gpt-image_2026-05-11_seed-1234.png
```

## Review Checklist

Before marking work complete:

- The artifact clearly maps to one pipeline mode.
- The four anchors are present.
- It avoids all forbidden moves in `docs/visual-bible-v2.md`.
- It uses or extends `src/styles/tokens.css`.
- It works without remote assets.
- It has been checked at desktop and mobile widths.
- Any verification gaps are recorded in `docs/completion-audit.md`.
