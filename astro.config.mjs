// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://felipemai3r.github.io',
  base: '/Projeto_Udesc_Make',
  vite: {
    plugins: [tailwindcss()]
  }
});