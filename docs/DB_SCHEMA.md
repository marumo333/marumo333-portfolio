# Database Schema (Supabase / PostgreSQL)

## Table: profiles
- id: uuid (Primary Key, references auth.users.id)
- role: text (default: 'user')
- bio: text
- avatar_url: text
- updated_at: timestamp

## Table: skills
- id: uuid (PK, default: gen_random_uuid())
- name: text (NOT NULL) - スキル名（例: "Python", "SvelteKit"）
- category: text (NOT NULL) - カテゴリ（例: "Frontend", "Backend", "Infrastructure"）
- level: integer (1-5) - 習熟度（1: 入門, 5: エキスパート）
- years_of_experience: numeric - 経験年数
- description: text - 補足説明
- icon_url: text - アイコン画像URL（任意）
- display_order: integer (default: 0) - 表示順
- created_at: timestamp (default: now())
- updated_at: timestamp (default: now())

## Table: careers
- id: uuid (PK, default: gen_random_uuid())
- company_name: text (NOT NULL) - 会社名
- position: text (NOT NULL) - 役職・ポジション
- start_date: date (NOT NULL) - 開始日
- end_date: date - 終了日（NULLの場合は現職）
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
- start_date: date - 開発開始日
- end_date: date - 開発終了日
- is_featured: boolean (default: false) - 注目プロダクトフラグ
- display_order: integer (default: 0) - 表示順
- created_at: timestamp (default: now())
- updated_at: timestamp (default: now())

## Table: chat_logs
- id: uuid (PK)
- user_id: uuid (FK -> profiles.id)
- message: text
- sender: text ('user' | 'ai')
- created_at: timestamp

---

## ER図（簡易）

```
profiles (1) ──── (N) chat_logs

skills      ← 独立テーブル（ポートフォリオオーナーのスキル）
careers     ← 独立テーブル（ポートフォリオオーナーの経歴）
products    ← 独立テーブル（ポートフォリオオーナーの開発実績）
```

※ skills, careers, products はポートフォリオオーナー（開発者自身）専用のため、user_idは不要。