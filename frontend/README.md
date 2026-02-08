# marumo333 Portfolio - Frontend

SvelteKit (Svelte 5) + Tailwind CSS v4 で構築されたポートフォリオサイトのフロントエンド。

## 技術スタック

- **Framework:** SvelteKit (Svelte 5)
- **CSS:** Tailwind CSS v4（`@tailwindcss/forms`, `@tailwindcss/typography`）
- **Language:** TypeScript (strict mode)
- **Build Tool:** Vite 7
- **Linter/Formatter:** ESLint 9 + Prettier

## 開発環境

### Docker（推奨）

プロジェクトルートで実行:

```sh
docker compose up
```

http://localhost:5173 でアクセス可能。Backend（FastAPI）との通信はViteプロキシ経由。

### ローカル

```sh
npm install
npm run dev
```

## スクリプト

| コマンド | 説明 |
|---------|------|
| `npm run dev` | 開発サーバー起動 |
| `npm run build` | プロダクションビルド |
| `npm run preview` | ビルド結果のプレビュー |
| `npm run check` | svelte-check（型チェック） |
| `npm run lint` | Prettier + ESLint |
| `npm run format` | Prettier によるフォーマット |

## ディレクトリ構成

```
src/
├── app.css                 # グローバルCSS、Tailwind @theme設定
├── app.d.ts                # SvelteKit型定義
├── app.html                # HTMLテンプレート
├── lib/
│   ├── index.ts
│   ├── assets/
│   │   └── favicon.svg
│   └── components/
│       └── ui/
│           ├── TypewriterText.svelte    # タイピングアニメーション
│           └── PageWithOpening.svelte   # オープニング付きページテンプレート
└── routes/
    ├── +layout.svelte      # 共通レイアウト（Header, Footer）
    ├── +page.svelte        # / (ホーム)
    ├── skills/             # /skills
    ├── career/             # /career
    ├── products/           # /products
    └── login/              # /login
```
