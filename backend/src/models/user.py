from typing import Optional, Dict, Any
from sqlmodel import Field, SQLModel, Relationship, Column, JSON
from .tenant_base import TenantBase

class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    additional_info: Optional[Dict[str, Any]] = Field(default=None, sa_column=Column(JSON))

class User(UserBase, TenantBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    lessons: list["Lesson"] = Relationship(back_populates="user")
    personalized_content: list["PersonalizedContent"] = Relationship(back_populates="user")

