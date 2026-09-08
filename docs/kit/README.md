# Kit

The two files a design system actually needs to ship, plus how to get them.

## What is here

- `tokens.css`: self-contained CSS custom properties. Dark-first `:root`, a `[data-theme="light"]` override, the full palette including the 20-swatch Nous blue monochrome set (`--color-nous-*`), typography, spacing, radius, shadows, motion, z-index, breakpoints.
- `tokens.json`: the same values in W3C design-token format, with a `$description` on every group. The Nous blue swatches carry their provenance in that field: eye-curated from the Nous Brand Booklet First Edition (2024), which prints no hex codes.

Both are copies of `src/styles/tokens.css` and `src/tokens/tokens.json` in this repository.

## Use it in five minutes

Link the stylesheet and use the variables.

```html
<link rel="stylesheet" href="https://thedavidmurray.github.io/nous-inspired-design-system/kit/tokens.css">
<div style="background: var(--color-nous-deepest); color: var(--color-nous-pale-icy); padding: 2rem">
  One ink, then restraint.
</div>
```

Or install the whole package (tokens, Tailwind preset, components) from the GitHub tarball. The package is not on npm.

```sh
pnpm add https://github.com/thedavidmurray/nous-inspired-design-system/tarball/main
```

## Make it yours

1. Replace the color values in `tokens.css`. Keep the names; the names are the contract.
2. Write your lexicon: the five to ten words your brand actually uses.
3. Write your palette bank: three to five named inks.
4. Keep the recipes and the guards described in [Method](../method.html). Roll prompts, keep the sentences that stay true, number them.

Unofficial. Inspired by Nous Research; not affiliated with or endorsed by them.
