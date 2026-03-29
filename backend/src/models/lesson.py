from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from .tenant_base import TenantBase

class LessonBase(SQLModel):
    content: str
    summary: Optional[str] = None
    is_summary_generated: bool = False

class Lesson(LessonBase, TenantBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    # Relationships
    user: Optional["User"] = Relationship(back_populates="lessons")
    personalized_content: list["PersonalizedContent"] = Relationship(back_populates="lesson")
