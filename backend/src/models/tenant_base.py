from typing import Optional
from sqlmodel import Field, SQLModel

class TenantBase(SQLModel):
    tenant_id: str = Field(index=True)
