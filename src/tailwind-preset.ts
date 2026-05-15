/**
 * Edgeless Lab Design System — Tailwind CSS Preset
 *
 * Usage in consumer tailwind.config.ts:
 *   import edgelessPreset from '@edgelesslab/design-system/tailwind';
 *   export default { presets: [edgelessPreset], ... }
 *
 * Or CommonJS:
 *   presets: [require('@edgelesslab/design-system/tailwind')]
 */

import type { Config } from 'tailwindcss';
import { tokens } from './tokens';

// Helper: strip `as const` readonly from token tuples so they satisfy Tailwind's mutable tuple types
function mutable<T>(value: T): { -readonly [K in keyof T]: T[K] } {
  return value as { -readonly [K in keyof T]: T[K] };
}

const edgelessPreset: Config = {
  darkMode: 'class',
  content: [],
  theme: {
    extend: {
      // === COLORS ===
      colors: {
        background: { ...tokens.colors.background },
        foreground: { ...tokens.colors.foreground },
        accent: {
          DEFAULT: tokens.colors.accent.primary,
          secondary: tokens.colors.accent.secondary,
          tertiary: tokens.colors.accent.tertiary,
        },
        border: { ...tokens.colors.border },
        success: tokens.colors.success,
        warning: tokens.colors.warning,
        error: tokens.colors.error,
        info: tokens.colors.info,
      },

      // === TYPOGRAPHY ===
      fontFamily: {
        sans: tokens.typography.fontFamily.sans.split(','),
        mono: tokens.typography.fontFamily.mono.split(','),
        display: tokens.typography.fontFamily.display.split(','),
      },
      fontSize: {
        xs: mutable(tokens.typography.fontSize.xs),
        sm: mutable(tokens.typography.fontSize.sm),
        base: mutable(tokens.typography.fontSize.base),
        lg: mutable(tokens.typography.fontSize.lg),
        xl: mutable(tokens.typography.fontSize.xl),
        '2xl': mutable(tokens.typography.fontSize['2xl']),
        '3xl': mutable(tokens.typography.fontSize['3xl']),
        '4xl': mutable(tokens.typography.fontSize['4xl']),
        '5xl': mutable(tokens.typography.fontSize['5xl']),
        '6xl': mutable(tokens.typography.fontSize['6xl']),
        '7xl': mutable(tokens.typography.fontSize['7xl']),
      },
      fontWeight: { ...tokens.typography.fontWeight },
      letterSpacing: { ...tokens.typography.letterSpacing },

      // === SPACING ===
      spacing: { ...tokens.spacing },

      // === RADIUS ===
      borderRadius: { ...tokens.radius },

      // === SHADOWS ===
      boxShadow: {
        sm: tokens.shadows.sm,
        DEFAULT: tokens.shadows.md,
        md: tokens.shadows.md,
        lg: tokens.shadows.lg,
        xl: tokens.shadows.xl,
        glow: tokens.shadows.glow,
        'glow-lg': tokens.shadows['glow-lg'],
      },

      // === ANIMATION ===
      transitionDuration: { ...tokens.motion.duration },
      transitionTimingFunction: {
        DEFAULT: tokens.motion.ease.default,
        in: tokens.motion.ease.in,
        out: tokens.motion.ease.out,
        bounce: tokens.motion.ease.bounce,
      },

      // === Z-INDEX ===
      zIndex: Object.fromEntries(
        Object.entries(tokens.zIndex).map(([k, v]) => [k, String(v)])
      ),

      // === BREAKPOINTS ===
      screens: { ...tokens.breakpoints },

      // === BACKGROUNDS ===
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-accent': tokens.colors.accent.gradient,
      },
    },
  },
};

export default edgelessPreset;
