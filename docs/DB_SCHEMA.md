# Database Schema (Supabase / PostgreSQL)

## Table: profiles
- id: uuid (Primary Key, references auth.users.id)
- role: text (default: 'user')
- bio: text
- avatar_url: text
- created_at: timestamp (default: now())
- updated_at: timestamp (default: now())

## Table: skills
- id: uuid (PK, default: gen_random_uuid())
- name: text (NOT NULL) - スキル名（例: "Python", "SvelteKit"）
- category: text (NOT NULL) - カテゴリ（例: "Frontend", "Backend", "Infrastructure"）
- level: integer (1-5) - 習熟度（1: 入門, 5: エキスパート）
- years_of_experience: numeric - 経験年数（例: 1.5）
- description: text - 補足説明
- icon_url: text - アイコン画像URL（任意）
- display_order: integer (default: 0) - 表示順
- created_at: timestamp (default: now())
- updated_at: timestamp (default: now())

## Table: careers
- id: uuid (PK, default: gen_random_uuid())
- company_name: text (NOT NULL) - 会社・組織名
- position: text (NOT NULL) - 役職・担当
- period_start: date (NOT NULL) - 在籍期間（開始）
- period_end: date - 在籍期間（終了）※NULLの場合は現職
- description: text - 業務内容・実績
- technologies: text[] - 使用技術（配列）
- display_order: integer (default: 0) - 表示順
- created_at: timestamp (default: now())
- updated_at: timestamp (default: now())

## Table: products
- id: uuid (PK, default: gen_random_uuid())
- name: text (NOT NULL) - プロダクト名
- description: text (NOT NULL) - 説明
- technologies: text[] - 使用技術（配列）
- image_url: text - サムネイル画像URL
- github_url: text - GitHubリポジトリURL
- demo_url: text - デモサイトURL
- period_start: date - 開発期間（開始）
- period_end: date - 開発期間（終了）
- is_featured: boolean (default: false) - 注目プロダクトフラグ
- display_order: integer (default: 0) - 表示順
- created_at: timestamp (default: now())
- updated_at: timestamp (default: now())

## Table: chat_logs
- id: uuid (PK, default: gen_random_uuid())
- user_id: uuid (FK -> profiles.id)
- message: text (NOT NULL)
- sender: text (NOT NULL) - 'user' | 'ai'
- created_at: timestamp (default: now())

---

## ER図（簡易）

```
profiles (1) ──── (N) chat_logs

skills      ← 独立テーブル（ポートフォリオオーナーのスキル）
careers     ← 独立テーブル（ポートフォリオオーナーの経歴）
products    ← 独立テーブル（ポートフォリオオーナーの開発実績）
```

※ skills, careers, products はポートフォリオオーナー（開発者自身）専用のため、user_idは不要。