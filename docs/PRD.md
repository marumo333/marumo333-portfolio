# Project Name: AI-Integrated Portfolio (SvelteKit x FastAPI)

## 1. プロジェクト概要
ユーザー（開発者自身）の経歴・スキルを公開するポートフォリオサイトに加え、認証済みユーザーのみが利用できる「本人を模したAIとのチャット機能」を持つWebアプリケーション。
本プロジェクトは、開発者がモダンなWeb開発技術（SvelteKit, FastAPI, Tailwind CSS, Supabase, Docker）をキャッチアップし、エンジニアとして自走力をつけるための学習用プロダクトである。

## 2. 目的・ゴール
* **プロダクト:** 自身のスキルを証明し、興味を持った人がAIを通じて詳細な経歴や考えを聞き出せる場を作る。
* **学習 (最重要):**
    * **Frontend:** SvelteKit (Svelte 5), Tailwind CSS v4の習得。
    * **Backend:** Python (FastAPI) の設計、型安全な実装、JWT認証の理解。
    * **Infra/Dev:** Docker環境構築、BFFパターンの理解。
    * **AI:** RAG (Retrieval-Augmented Generation) の実装。

## 3. 技術スタック
* **Frontend:** SvelteKit (TypeScript), Tailwind CSS (v4), @tailwindcss/typography
* **Backend:** Python 3.11, FastAPI, Pydantic (v2)
* **Database / Auth:** Supabase (PostgreSQL, GoTrue)
* **Environment:** Docker Compose (Frontend & Backend Hot-reloading)
* **Infrastructure:** (将来的に) Vercel + Renderなど

## 4. 機能要件
### Phase 1: 静的ポートフォリオ (MVP)
* **トップページ:** ヒーローセクション、自己紹介。
* **経歴表示:** バックエンドAPIから取得したプロフィールデータの表示。
* **UI:** Tailwind CSSを用いたモダンでレスポンシブなデザイン。

### Phase 2: 認証とセキュリティ
* **ログイン機能:** Supabase Authを用いた認証。
* **アクセス制御:** 未ログイン時はチャット不可、ログイン時のみチャット画面へ遷移。
* **セキュリティ:** Frontend(SvelteKit)を経由したBFF構成、もしくはFastAPI側でのJWT検証。

### Phase 3: AIチャット (RAG)
* **チャットUI:** ユーザー入力とAI回答の対話インターフェース。
* **ストリーミング回答:** AIの思考をリアルタイムで表示。
* **コンテキスト認識:** 開発者の経歴データを踏まえた回答生成。

## 5. デザイン・UX方針
* シンプルかつ「エンジニアらしい」整ったUI。
* CSS学習のため、安易なUIライブラリ（DaisyUI等）には頼らず、TailwindのUtility ClassとCSSの基礎概念（Flexbox/Grid）を理解して実装する。