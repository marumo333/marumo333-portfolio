# Tech Stack & Coding Rules

## Frontend Rules
- **Framework:** SvelteKit (Svelte 5)
- **State Management:** Use Runes (`$state`, `$derived`, `$effect`) ONLY. Do not use `export let` for props (use `$props()`).
- **CSS:** Tailwind CSS v4.
  - Configuration: Use CSS-first configuration (`@theme` in CSS), NOT `tailwind.config.js`.
  - Plugins: `@tailwindcss/forms`, `@tailwindcss/typography`（`app.css` で `@plugin` 宣言）。
  - Styling: Use utility classes primarily. Use `<article class="prose">` for markdown content.
  - Global CSS: `src/app.css` に集約。ページ固有のCSSファイルは作成しない。
- **Language:** TypeScript (strict mode). Use `type` alias over `interface`.
- **Navigation:** Use `resolve()` from `$app/paths` for internal links.
- **Build Tool:** Vite 7 + `@tailwindcss/vite` プラグイン。
- **Linter/Formatter:** ESLint 9 + Prettier（`prettier-plugin-svelte`, `prettier-plugin-tailwindcss`）。

## Component Design Rules
- **Single File Component:** UIとロジックは1つの`.svelte`ファイルに統合（Svelte推奨パターン）。
- **Reusable Components:** `$lib/components/ui/` に配置。
- **Props:** `type Props = { ... }` で型定義し、`$props()` で受け取る。
- **Children:** Svelte 5の `Snippet` を使用。`{@render children()}` でレンダリング。
- **分離の基準:** コンポーネントが100行を超える、または複数箇所で再利用する場合のみ分離を検討。

## Backend Rules
- **Framework:** FastAPI
- **Language:** Python 3.12（`pyproject.toml` の `target-version`）
- **Validation:** Pydantic v2 (`model_config`, `field_validator`).
- **Type Hinting:** Python 3.10+ syntax (Use `str | None` instead of `Optional[str]`).
- **Docstring:** Google Style.
- **Linter:** Ruff（E, W, F, I, B, C4, UP ルール有効）。`line-length = 88`。
- **Type Checker:** Mypy strict mode（`pydantic.mypy` プラグイン使用）。
- **Alias:** レスポンスモデルはcamelCaseエイリアス（`pydantic.alias_generators.to_camel`）。
- **Database:** Supabase（`supabase-py` クライアント経由）。環境変数 `SUPABASE_URL`, `SUPABASE_KEY` で接続。

## Architecture Rules
- **BFF Pattern:** Frontend (SvelteKit) talks to Backend (FastAPI) via Vite Dev Server Proxy (`/api` → `http://backend:8000`).
- **API Prefix:** Backend の全APIルーターは `/api` prefix を使用。
- **Auth:** Supabase Auth. Backend validates JWT using `pyjwt`.
- **Docker:** `docker-compose.yml` で frontend / backend を同一ネットワークに配置。ホットリロード対応。
- **CI:** GitHub Actions で lint / type check を自動実行（backend: Ruff + Mypy, frontend: svelte-check + ESLint + Prettier）。