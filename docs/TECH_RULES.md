# Tech Stack & Coding Rules

## Frontend Rules
- **Framework:** SvelteKit (Svelte 5)
- **State Management:** Use Runes (`$state`, `$derived`, `$effect`) ONLY. Do not use `export let` for props (use `$props()`).
- **CSS:** Tailwind CSS v4.
  - Configuration: Use CSS-first configuration (`@theme` in CSS), NOT `tailwind.config.js`.
  - Styling: Use utility classes primarily. Use `<article class="prose">` for markdown content.
  - Global CSS: `src/app.css` に集約。ページ固有のCSSファイルは作成しない。
- **Language:** TypeScript. Use `type` alias over `interface`.
- **Navigation:** Use `resolve()` from `$app/paths` for internal links.

## Component Design Rules
- **Single File Component:** UIとロジックは1つの`.svelte`ファイルに統合（Svelte推奨パターン）。
- **Reusable Components:** `$lib/components/ui/` に配置。
- **Props:** `type Props = { ... }` で型定義し、`$props()` で受け取る。
- **Children:** Svelte 5の `Snippet` を使用。`{@render children()}` でレンダリング。
- **分離の基準:** コンポーネントが100行を超える、または複数箇所で再利用する場合のみ分離を検討。

## Backend Rules
- **Framework:** FastAPI
- **Validation:** Pydantic v2 (`model_config`, `field_validator`).
- **Type Hinting:** Python 3.10+ syntax (Use `str | None` instead of `Optional[str]`).
- **Docstring:** Google Style.

## Architecture Rules
- **BFF Pattern:** Frontend (SvelteKit) talks to Backend (FastAPI) via Server Proxy.
- **Auth:** Supabase Auth. Backend validates JWT using `pyjwt`.