# Tech Stack & Coding Rules

## Frontend Rules
- **Framework:** SvelteKit (Svelte 5)
- **State Management:** Use Runes (`$state`, `$derived`, `$effect`) ONLY. Do not use `export let` for props (use `$props()`).
- **CSS:** Tailwind CSS v4.
  - Configuration: Use CSS-first configuration (`@theme` in CSS), NOT `tailwind.config.js`.
  - Styling: Use utility classes primarily. Use `<article class="prose">` for markdown content.
- **Language:** TypeScript. Use `type` alias over `interface`.

## Backend Rules
- **Framework:** FastAPI
- **Validation:** Pydantic v2 (`model_config`, `field_validator`).
- **Type Hinting:** Python 3.10+ syntax (Use `str | None` instead of `Optional[str]`).
- **Docstring:** Google Style.

## Architecture Rules
- **BFF Pattern:** Frontend (SvelteKit) talks to Backend (FastAPI) via Server Proxy.
- **Auth:** Supabase Auth. Backend validates JWT using `pyjwt`.