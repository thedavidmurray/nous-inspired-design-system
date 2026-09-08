import type { Config } from 'tailwindcss';
import { tokens } from './src/tokens';

const config: Config = {
  darkMode: 'class',
  content: [
    './src/**/*.{js,ts,jsx,tsx,mdx}',
    './public/**/*.html',
  ],
  theme: {
    extend: {
      // === COLORS ===
      colors: {
        background: tokens.colors.background,
        foreground: tokens.colors.foreground,
        accent: {
          DEFAULT: tokens.colors.accent.primary,
          secondary: tokens.colors.accent.secondary,
          tertiary: tokens.colors.accent.tertiary,
        },
        border: tokens.colors.border,
        success: tokens.colors.success,
        warning: tokens.colors.warning,
        error: tokens.colors.error,
        info: tokens.colors.info,
        nous: tokens.colors.nous,
        duotone: tokens.colors.duotone,
      },
      
      // === TYPOGRAPHY ===
      fontFamily: {
        sans: tokens.typography.fontFamily.sans.split(','),
        mono: tokens.typography.fontFamily.mono.split(','),
        display: tokens.typography.fontFamily.display.split(','),
        intel: tokens.typography.fontFamily.intel.split(','),
        editorial: tokens.typography.fontFamily.editorial.split(','),
        'display-serif': tokens.typography.fontFamily['display-serif'].split(','),
        bitmap: tokens.typography.fontFamily.bitmap.split(','),
      },
      fontSize: {
        xs: tokens.typography.fontSize.xs,
        sm: tokens.typography.fontSize.sm,
        base: tokens.typography.fontSize.base,
        lg: tokens.typography.fontSize.lg,
        xl: tokens.typography.fontSize.xl,
        '2xl': tokens.typography.fontSize['2xl'],
        '3xl': tokens.typography.fontSize['3xl'],
        '4xl': tokens.typography.fontSize['4xl'],
        '5xl': tokens.typography.fontSize['5xl'],
        '6xl': tokens.typography.fontSize['6xl'],
        '7xl': tokens.typography.fontSize['7xl'],
      },
      fontWeight: tokens.typography.fontWeight,
      letterSpacing: tokens.typography.letterSpacing,
      
      // === SPACING ===
      spacing: tokens.spacing,
      
      // === RADIUS ===
      borderRadius: tokens.radius,
      
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
      transitionDuration: tokens.motion.duration,
      transitionTimingFunction: {
        DEFAULT: tokens.motion.ease.default,
        in: tokens.motion.ease.in,
        out: tokens.motion.ease.out,
        bounce: tokens.motion.ease.bounce,
      },
      
      // === Z-INDEX ===
      zIndex: tokens.zIndex,
      
      // === BREAKPOINTS ===
      screens: tokens.breakpoints,
      
      // === BACKGROUNDS ===
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-accent': tokens.colors.accent.gradient,
      },
    },
  },
  plugins: [
    // Custom utilities
    ({ addUtilities }) => {
      addUtilities({
        '.text-balance': {
          'text-wrap': 'balance',
        },
        '.glow-accent': {
          'box-shadow': tokens.shadows.glow,
        },
        '.glow-accent-lg': {
          'box-shadow': tokens.shadows['glow-lg'],
        },
        '.surface-elevated': {
          'background-color': tokens.colors.background.elevated,
          'border': `1px solid ${tokens.colors.border.default}`,
          'border-radius': tokens.radius.lg,
        },
        '.surface-glass': {
          'background-color': 'rgba(17, 17, 17, 0.8)',
          'backdrop-filter': 'blur(12px)',
          'border': `1px solid ${tokens.colors.border.subtle}`,
        },
      });
    },
  ],
};

export default config;
