import { defineConfig } from "vite";
import path, { dirname } from "node:path";
import solid from "vite-plugin-solid";

dirname;
export default defineConfig({
  plugins: [solid()],
  resolve: {
    alias: [
      { find: "@solid-ui", replacement: "/src/components/solid-ui" },
      { find: "@assets", replacement: "/src/assets" },
      { find: "@components", replacement: "/src/components" },
      { find: "@pages", replacement: "/src/pages" },
      { find: "@providers", replacement: "/src/providers" },
      { find: "@utils", replacement: "/src/utils" },
      { find: "@styles", replacement: "/src/styles" },
    ],
  },
});
