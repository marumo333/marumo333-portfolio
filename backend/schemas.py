"""API レスポンス用 Pydantic スキーマ定義モジュール

このモジュールはポートフォリオAPIのレスポンススキーマを定義
すべてのスキーマはキャメルケースのエイリアスを使用し、ORMモデルからの変換に対応
"""

from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ProfileResponse(BaseModel):
    """ユーザープロフィールのレスポンススキーマ.

    Attributes:
        id: ユーザーの一意識別子（Supabase Auth user_id）
        role: ユーザーの権限ロール（例: "user", "admin"）
        bio: 自己紹介文
        avatar_url: プロフィール画像のURL
        created_at: プロフィール作成日時
        updated_at: プロフィール更新日時
    """

    id: UUID
    role: str
    bio: str | None = None
    avatar_url: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )


class SkillsResponse(BaseModel):
    """スキル情報のレスポンススキーマ.

    Attributes:
        id: スキルの一意識別子
        name: スキル名（例: "Python", "SvelteKit"）
        category: スキルカテゴリ（例: "Frontend", "Backend", "Infrastructure"）
        level: 習熟度（1: 入門 〜 5: エキスパート）
        years_of_experience: 経験年数（小数対応、例: 1.5）
        description: スキルの補足説明
        icon_url: スキルアイコン画像のURL
        display_order: 表示順序（昇順）
        created_at: レコード作成日時
        updated_at: レコード更新日時
    """

    id: UUID
    name: str
    category: str
    level: int
    years_of_experience: int | float
    description: str | None = None
    icon_url: str | None = None
    display_order: int
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )


class CareerResponse(BaseModel):
    """経歴情報のレスポンススキーマ.

    Attributes:
        id: 経歴の一意識別子
        company_name: 会社・組織名
        position: 役職・担当ポジション
        period_start: 在籍期間の開始日
        period_end: 在籍期間の終了日（Noneの場合は現職）
        description: 業務内容・実績の説明
        technologies: 使用技術のリスト
        created_at: レコード作成日時
        updated_at: レコード更新日時
    """

    id: UUID
    company_name: str
    position: str
    period_start: date
    period_end: date | None = None
    description: str | None = None
    technologies: list[str] | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )


class ProductsResponse(BaseModel):
    """開発実績のレスポンススキーマ.

    Attributes:
        id: プロダクトの一意識別子
        name: プロダクト名
        description: プロダクトの説明
        technologies: 使用技術のリスト
        image_url: サムネイル画像のURL
        github_url: GitHubリポジトリのURL
        period_start: 開発期間の開始日
        period_end: 開発期間の終了日
    """

    id: UUID
    name: str
    description: str
    technologies: list[str] | None = None
    image_url: str | None = None
    github_url: str | None = None
    period_start: date
    period_end: date | None = None

    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )


class ChatLogsResponse(BaseModel):
    """チャット履歴のレスポンススキーマ.

    Attributes:
        id: チャットログの一意識別子
        user_id: チャットを行ったユーザーのID
        message: メッセージ本文
        sender: 送信者種別（"user" または "ai"）
        created_at: メッセージ送信日時
    """

    id: UUID
    user_id: UUID
    message: str
    sender: str
    created_at: datetime

    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )
