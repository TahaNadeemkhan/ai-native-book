import os
from typing import Generator

from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv

# Import all models to ensure they are registered with SQLModel.metadata
from src.models.user import User
from src.models.lesson import Lesson
from src.models.personalized_content import PersonalizedContent
from src.models.tenant_base import TenantBase

load_dotenv() # Load environment variables here

database_url = os.environ.get("DATABASE_URL")


engine = create_engine(database_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

if __name__ == "__main__":
    print("Creating database and tables...")
    create_db_and_tables()
    print("Database and tables created.")
