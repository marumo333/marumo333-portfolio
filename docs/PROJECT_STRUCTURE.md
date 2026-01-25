# Project Structure

```
.
├── docker-compose.yml
├── backend
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── docs
│   ├── DB_SCHEMA.md
│   ├── PRD.md
│   ├── PROJECT_STRUCTURE.md
│   └── TECH_RULES.md
└── frontend
    ├── Dockerfile
    ├── package.json
    ├── vite.config.ts
    ├── svelte.config.js
    ├── tsconfig.json
    ├── .prettierrc
    ├── eslint.config.js
    ├── src
    │   ├── app.css              # グローバルCSS、Tailwind @theme設定
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
    │       ├── +layout.svelte   # 共通レイアウト（Header, Footer）
    │       ├── +page.svelte     # / (ホーム)
    │       ├── skills
    │       │   └── +page.svelte # /skills
    │       ├── career
    │       │   └── +page.svelte # /career
    │       ├── products
    │       │   └── +page.svelte # /products
    │       └── login
    │           └── +page.svelte # /login
    └── static
        └── robots.txt
```

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
| `/skills` | `skills/+page.svelte` | スキル一覧 |
| `/career` | `career/+page.svelte` | 経歴 |
| `/products` | `products/+page.svelte` | 開発実績 |
| `/login` | `login/+page.svelte` | ログイン |