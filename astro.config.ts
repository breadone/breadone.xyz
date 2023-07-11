import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import tailwind from "@astrojs/tailwind";
// import image from "@astrojs/image";
import sitemap from "@astrojs/sitemap";
import prefetch from "@astrojs/prefetch";

import node from "@astrojs/node";

// https://astro.build/config
export default defineConfig({
  site: "https://breadone.xyz",
  experimental: {
    assets: true
   },
  markdown: {
    shikiConfig: {
      theme: "dracula",
      wrap: true
    }
  },
  integrations: [mdx({}), tailwind({
    applyBaseStyles: false
  }), sitemap(), prefetch()],
  compressHTML: true,
  vite: {
    optimizeDeps: {
      exclude: ["@resvg/resvg-js"]
    }
  },
  output: "hybrid",
  adapter: node({
    mode: "standalone"
  })
});