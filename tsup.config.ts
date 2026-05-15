import { defineConfig } from 'tsup';
import { cpSync, mkdirSync } from 'fs';

export default defineConfig({
  entry: {
    index: 'src/index.ts',
    'tokens/index': 'src/tokens/index.ts',
    'components/index': 'src/components/index.ts',
    'utils/cn': 'src/utils/cn.ts',
    'tailwind-preset': 'src/tailwind-preset.ts',
  },
  format: ['esm', 'cjs'],
  dts: true,
  sourcemap: true,
  clean: true,
  external: ['react', 'react-dom', 'tailwindcss'],
  outDir: 'dist',
  banner: {
    js: '"use client";',
  },
  onSuccess: async () => {
    // Copy globals.css to dist/styles/ so the "./styles" export resolves
    mkdirSync('dist/styles', { recursive: true });
    cpSync('src/styles/globals.css', 'dist/styles/globals.css');
  },
});
