# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

```bash
npm run dev          # Start dev server at http://localhost:3000
npm run build        # Production build
npm run generate     # Static site generation
npm run preview      # Preview production build locally
npm run lint         # ESLint (delegates to generated ./.nuxt/eslint.config.mjs)
npm run format       # Prettier
```

### Verification Scripts

```bash
# Both scripts require Playwright (pip install playwright && playwright install chromium)
# Dev server must be running on port 3000 first
python scripts/verify_homepage.py           # Screenshot + content checks on desktop/mobile
python scripts/verify_nuxt_ui.py            # Assert @nuxt/ui components present in templates
```

## Architecture

### Nuxt 4 directory convention

This project uses the Nuxt 4 `app/` source root. Directories like `pages/`, `layouts/`, `composables/`, `stores/` live **inside `app/`**, not at the project root. The root-level `nuxt.config.ts` is the only Nuxt config file at the top level.

### Module stack

Three Nuxt modules are registered in `nuxt.config.ts`:

- **`@nuxt/ui`** — provides components (`UApp`, `UButton`, `UCard`, `UIcon`) and configures Tailwind CSS v4. Tailwind v4 uses CSS-first configuration (`@import "tailwindcss"` in `app/assets/styles/main.css`), not a separate `tailwind.config.js`. `UApp` must wrap the entire app in `app/app.vue` — this is required by the module.
- **`@pinia/nuxt`** — auto-imports `defineStore` and `useXxxStore` globally. Stores defined in `app/stores/` are usable in any component without manual imports.
- **`@nuxt/eslint`** — generates `.nuxt/eslint.config.mjs` at dev/build time. The project's `eslint.config.mjs` simply re-exports that generated config.

### Auto-imports

Nuxt auto-imports from `app/composables/` and `app/stores/`. The composable `useApi<T>()` and store `useAppStore()` are used in `app/pages/index.vue` without explicit import statements. This is handled by Nuxt's build-time code generation (`.nuxt/imports.d.ts`).

### `useApi` composable

`app/composables/useApi.ts` wraps `useFetch` with `useRuntimeConfig().public.apiBase` injected as `baseURL`. Set `NUXT_PUBLIC_API_BASE` in `.env` to point to a different backend. If left empty (default), requests are relative (same-origin), hitting the Nitro server at `server/api/`.

### Nitro server

`server/api/health.get.ts` creates `GET /api/health` returning `{ ok: true, service: "nuxt-vue-project" }`. File naming follows Nitro convention: `name.method.extension` maps HTTP method + route.

### Styling

All styles are in `app/assets/styles/main.css`. The design uses CSS custom properties for the medical/healthcare teal-green palette (`--primary: #0891b2`, `--secondary: #10b981`, etc.). The main font stack uses `Noto Serif SC` for headings and system UI fonts for body. Responsive breakpoints at 980px and 640px.

### Static assets

Images in `public/static/` are referenced as `/static/...` in templates. All images are WebP format optimized for web delivery.
