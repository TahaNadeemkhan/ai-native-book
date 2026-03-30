from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from .tenant_base import TenantBase

class PersonalizedContentBase(SQLModel):
    content: str

class PersonalizedContent(PersonalizedContentBase, TenantBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    lesson_id: Optional[int] = Field(default=None, foreign_key="lesson.id")

    # Relationships
    user: Optional["User"] = Relationship(back_populates="personalized_content")
    lesson: Optional["Lesson"] = Relationship(back_populates="personalized_content")
