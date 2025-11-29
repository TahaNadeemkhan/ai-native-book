import pytest
from sqlmodel import Session, SQLModel, create_engine
from src.models.user import User
from src.models.tenant_base import TenantBase

# Setup for in-memory SQLite for testing
engine = create_engine("sqlite:///./test.db")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@pytest.fixture(name="session")
def session_fixture():
    create_db_and_tables()
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

def test_create_user(session: Session):
    user = User(email="test@example.com", tenant_id="tenant1", additional_info={"hardware": "GPU1", "proficiency": "beginner"})
    session.add(user)
    session.commit()
    session.refresh(user)

    assert user.id is not None
    assert user.email == "test@example.com"
    assert user.tenant_id == "tenant1"
    assert user.additional_info == {"hardware": "GPU1", "proficiency": "beginner"}

def test_read_user(session: Session):
    user_in = User(email="read@example.com", tenant_id="tenant2")
    session.add(user_in)
    session.commit()
    session.refresh(user_in)

    user_out = session.get(User, user_in.id)
    assert user_out.email == "read@example.com"
    assert user_out.tenant_id == "tenant2"

def test_update_user(session: Session):
    user_in = User(email="update@example.com", tenant_id="tenant3")
    session.add(user_in)
    session.commit()
    session.refresh(user_in)

    user_in.email = "updated_email@example.com"
    user_in.additional_info = {"new_info": "data"}
    session.add(user_in)
    session.commit()
    session.refresh(user_in)

    user_out = session.get(User, user_in.id)
    assert user_out.email == "updated_email@example.com"
    assert user_out.additional_info == {"new_info": "data"}

def test_delete_user(session: Session):
    user_in = User(email="delete@example.com", tenant_id="tenant4")
    session.add(user_in)
    session.commit()
    session.refresh(user_in)

    session.delete(user_in)
    session.commit()

    user_out = session.get(User, user_in.id)
    assert user_out is None
