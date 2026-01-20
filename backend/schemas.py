from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class ProfileResponse(BaseModel):
    id: UUID
    role: str
    bio: str |None = None
    avatar_url: str | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True, 
        from_attributes=True
    )