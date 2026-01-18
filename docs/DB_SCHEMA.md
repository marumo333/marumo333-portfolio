# Database Schema (Supabase / PostgreSQL)

## Table: profiles
- id: uuid (Primary Key, references auth.users.id)
- role: text (default: 'user')
- bio: text
- avatar_url: text
- updated_at: timestamp

## Table: chat_logs
- id: uuid (PK)
- user_id: uuid (FK -> profiles.id)
- message: text
- sender: text ('user' | 'ai')
- created_at: timestamp