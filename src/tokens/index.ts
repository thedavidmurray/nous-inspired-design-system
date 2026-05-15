/**
 * Edgeless Lab Design Tokens
 * 
 * Reference quality: Vercel, Linear, Raycast
 * Principles: High contrast, generous whitespace, purposeful motion
 */

// === COLOR TOKENS ===
export const colors = {
  // Primary palette - Deep void blacks, subtle warmth
  background: {
    primary: '#0a0a0a',      // Deepest void
    secondary: '#111111',    // Elevated surfaces
    tertiary: '#1a1a1a',     // Subtle distinction
    elevated: '#222222',     // Cards, modals
  },
  
  // Foreground - Crisp, accessible
  foreground: {
    primary: '#ffffff',      // 100% luminance
    secondary: 'rgba(255,255,255,0.7)',   // Body text
    tertiary: 'rgba(255,255,255,0.5)',     // Muted
    quaternary: 'rgba(255,255,255,0.25)',  // Disabled, hints
  },
  
  // Accent - Electric indigo to cyan gradient space
  accent: {
    primary: '#6366f1',      // Indigo 500
    secondary: '#8b5cf6',  // Violet 500
    tertiary: '#06b6d4',   // Cyan 500
    gradient: 'linear-gradient(135deg, #6366f1 0%, #06b6d4 100%)',
  },
  
  // Semantic - Clear status communication
  success: '#22c55e',      // Green 500
  warning: '#f59e0b',      // Amber 500
  error: '#ef4444',        // Red 500
  info: '#3b82f6',         // Blue 500
  
  // Border - Subtle depth
  border: {
    subtle: 'rgba(255,255,255,0.08)',
    default: 'rgba(255,255,255,0.12)',
    strong: 'rgba(255,255,255,0.2)',
  },
} as const;

// === TYPOGRAPHY TOKENS ===
export const typography = {
  // Font families - Geometric sans for UI, monospace for data
  fontFamily: {
    sans: 'Inter, system-ui, -apple-system, sans-serif',
    mono: 'JetBrains Mono, SF Mono, monospace',
    display: 'Cal Sans, Inter, sans-serif', // For headlines
  },
  
  // Scale - Major Third (1.25) progression
  fontSize: {
    xs: ['0.75rem', { lineHeight: '1rem' }],      // 12px
    sm: ['0.875rem', { lineHeight: '1.25rem' }],   // 14px
    base: ['1rem', { lineHeight: '1.5rem' }],     // 16px
    lg: ['1.125rem', { lineHeight: '1.75rem' }],   // 18px
    xl: ['1.25rem', { lineHeight: '1.75rem' }],    // 20px
    '2xl': ['1.5rem', { lineHeight: '2rem' }],    // 24px
    '3xl': ['1.875rem', { lineHeight: '2.25rem' }], // 30px
    '4xl': ['2.25rem', { lineHeight: '2.5rem' }], // 36px
    '5xl': ['3rem', { lineHeight: '1.1' }],       // 48px
    '6xl': ['3.75rem', { lineHeight: '1.1' }],    // 60px
    '7xl': ['4.5rem', { lineHeight: '1.05' }],    // 72px
  },
  
  // Weights - Restrained, purposeful
  fontWeight: {
    normal: '400',
    medium: '500',
    semibold: '600',
    bold: '700',
  },
  
  // Letter spacing - Tighter for display, looser for small
  letterSpacing: {
    tighter: '-0.05em',
    tight: '-0.025em',
    normal: '0',
    wide: '0.025em',
    wider: '0.05em',
  },
} as const;

// === SPACING TOKENS ===
export const spacing = {
  // 4px base grid, semantic naming
  0: '0',
  px: '1px',
  0.5: '0.125rem',  // 2px
  1: '0.25rem',     // 4px
  2: '0.5rem',      // 8px
  3: '0.75rem',     // 12px
  4: '1rem',        // 16px
  5: '1.25rem',     // 20px
  6: '1.5rem',      // 24px
  8: '2rem',        // 32px
  10: '2.5rem',     // 40px
  12: '3rem',       // 48px
  16: '4rem',       // 64px
  20: '5rem',       // 80px
  24: '6rem',       // 96px
  32: '8rem',       // 128px
  40: '10rem',      // 160px
  48: '12rem',      // 192px
  56: '14rem',      // 224px
  64: '16rem',      // 256px
} as const;

// === RADIUS TOKENS ===
export const radius = {
  none: '0',
  sm: '0.25rem',    // 4px
  md: '0.5rem',     // 8px
  lg: '0.75rem',    // 12px
  xl: '1rem',       // 16px
  '2xl': '1.5rem',  // 24px
  full: '9999px',   // Pills, circles
} as const;

// === SHADOW TOKENS ===
export const shadows = {
  // Subtle elevation on dark backgrounds
  sm: '0 1px 2px 0 rgba(0, 0, 0, 0.3)',
  md: '0 4px 6px -1px rgba(0, 0, 0, 0.4), 0 2px 4px -2px rgba(0, 0, 0, 0.3)',
  lg: '0 10px 15px -3px rgba(0, 0, 0, 0.5), 0 4px 6px -4px rgba(0, 0, 0, 0.3)',
  xl: '0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.4)',
  // Glow for accent elements
  glow: '0 0 20px rgba(99, 102, 241, 0.3)',
  'glow-lg': '0 0 40px rgba(99, 102, 241, 0.4)',
} as const;

// === MOTION TOKENS ===
export const motion = {
  // Duration - Snappy, purposeful
  duration: {
    fast: '100ms',
    normal: '200ms',
    slow: '300ms',
    slower: '500ms',
  },
  
  // Easing - Natural, premium feel
  ease: {
    default: 'cubic-bezier(0.4, 0, 0.2, 1)',
    in: 'cubic-bezier(0.4, 0, 1, 1)',
    out: 'cubic-bezier(0, 0, 0.2, 1)',
    bounce: 'cubic-bezier(0.34, 1.56, 0.64, 1)',
  },
} as const;

// === Z-INDEX SCALE ===
export const zIndex = {
  base: 0,
  dropdown: 100,
  sticky: 200,
  modal: 300,
  popover: 400,
  toast: 500,
  tooltip: 600,
} as const;

// === BREAKPOINTS ===
export const breakpoints = {
  sm: '640px',
  md: '768px',
  lg: '1024px',
  xl: '1280px',
  '2xl': '1536px',
} as const;

// Export all tokens as a unified object
export const tokens = {
  colors,
  typography,
  spacing,
  radius,
  shadows,
  motion,
  zIndex,
  breakpoints,
} as const;

export default tokens;
