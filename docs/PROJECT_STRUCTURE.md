# Project Structure

```
.
├── .github
│   └── workflows
│       ├── backend.yml          # Backend CI（Ruff, Mypy）
│       └── frontend.yml         # Frontend CI（svelte-check, ESLint, Prettier）
├── docker-compose.yml
├── backend
│   ├── .env                     # 環境変数（SUPABASE_URL, SUPABASE_KEY）※Git管理外
│   ├── Dockerfile
│   ├── main.py                  # FastAPIアプリケーション（CORS, ルーター登録）
│   ├── pyproject.toml           # Ruff / Mypy 設定
│   ├── requirements.txt
│   ├── schemas.py               # Pydantic v2 レスポンススキーマ定義
│   └── routers
│       ├── __init__.py
│       └── profile.py           # APIエンドポイント（profile, skills, careers, products）
├── docs
│   ├── DB_SCHEMA.md
│   ├── PRD.md
│   ├── PROJECT_STRUCTURE.md
│   └── TECH_RULES.md
└── frontend
    ├── .npmrc
    ├── .prettierrc
    ├── .prettierignore
    ├── Dockerfile
    ├── eslint.config.js
    ├── package.json
    ├── svelte.config.js
    ├── tsconfig.json
    ├── vite.config.ts             # Viteプロキシ設定（/api → backend:8000）
    ├── src
    │   ├── app.css                # グローバルCSS、Tailwind @theme設定
    │   ├── app.d.ts
    │   ├── app.html
    │   ├── lib
    │   │   ├── index.ts
    │   │   ├── assets
    │   │   │   └── favicon.svg
    │   │   └── components
    │   │       └── ui
    │   │           ├── TypewriterText.svelte    # タイピングアニメーション
    │   │           └── PageWithOpening.svelte   # オープニング付きページテンプレート
    │   └── routes
    │       ├── +layout.svelte     # 共通レイアウト（Header, Footer, ナビゲーション）
    │       ├── +page.svelte       # / (ホーム)
    │       ├── skills
    │       │   └── +page.svelte   # /skills（準備中）
    │       ├── career
    │       │   └── +page.svelte   # /career（準備中）
    │       ├── products
    │       │   └── +page.svelte   # /products（準備中）
    │       └── login
    │           └── +page.svelte   # /login（準備中）
    └── static
        └── robots.txt
```

## Backend 構成

### エントリーポイント: `main.py`
- FastAPIアプリケーション初期化
- CORSミドルウェア設定（`localhost:5173`, `127.0.0.1:5173`）
- ルーター登録（`profile.router`）

### routers/profile.py
Supabaseからデータを取得するAPIエンドポイント群（prefix: `/api`）

| エンドポイント | レスポンス型 | 説明 |
|---------------|-------------|------|
| `GET /api/profile/me` | `ProfileResponse` | プロフィール取得（単一） |
| `GET /api/skills` | `list[SkillsResponse]` | スキル一覧（display_order順） |
| `GET /api/careers` | `list[CareerResponse]` | 経歴一覧（display_order順） |
| `GET /api/products` | `list[ProductsResponse]` | 開発実績一覧（display_order順） |

### schemas.py
Pydantic v2によるレスポンススキーマ。全モデルでcamelCaseエイリアスを使用。

| スキーマ | 対応テーブル |
|---------|------------|
| `ProfileResponse` | profiles |
| `SkillsResponse` | skills |
| `CareerResponse` | careers |
| `ProductsResponse` | products |
| `ChatLogsResponse` | chat_logs |

## Frontend コンポーネント構成

### lib/components/ui/
再利用可能なUIコンポーネント

| コンポーネント | 説明 |
|---------------|------|
| `TypewriterText.svelte` | タイピングアニメーション。文字数に応じて自動調整 |
| `PageWithOpening.svelte` | オープニングアニメーション付きページテンプレート |

### routes/
SvelteKitのファイルベースルーティング

| パス | ファイル | 説明 |
|------|----------|------|
| `/` | `+page.svelte` | ホーム（ヒーローセクション） |
| `/skills` | `skills/+page.svelte` | スキル一覧（準備中） |
| `/career` | `career/+page.svelte` | 経歴（準備中） |
| `/products` | `products/+page.svelte` | 開発実績（準備中） |
| `/login` | `login/+page.svelte` | ログイン（準備中） |

## CI/CD

| ワークフロー | トリガー | 実行内容 |
|-------------|---------|---------|
| `backend.yml` | `backend/**` の変更時 | Ruff lint/format, Mypy型チェック |
| `frontend.yml` | `frontend/**` の変更時 | svelte-check, ESLint, Prettier |

## Docker構成

| サービス | ポート | ベースイメージ | 備考 |
|---------|-------|--------------|------|
| backend | 8000 | python:3.11-slim | uvicorn --reload（ホットリロード） |
| frontend | 5173 | node:20-slim | vite dev --host |

frontendからbackendへの通信はViteプロキシ（`/api` → `http://backend:8000`）経由。