import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine, select
from src.main import app
from src.database import get_session
from src.models.user import User

# Setup for in-memory SQLite for testing
sqlite_file_name = "test.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

@pytest.fixture(name="session")
def session_fixture():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

def test_github_oauth_callback_and_onboarding(client: TestClient, session: Session):
    # Simulate GitHub OAuth callback
    test_code = "mock_github_code_123"
    response = client.post(f"/auth/github-callback?code={test_code}")
    assert response.status_code == 200
    auth_data = response.json()
    assert "access_token" in auth_data
    assert auth_data["token_type"] == "bearer"

    # Verify user creation
    user_email = f"user_{test_code}@github.com"
    user = session.exec(select(User).where(User.email == user_email)).first()
    assert user is not None
    assert user.tenant_id == "default_tenant"

    # Simulate onboarding profile update
    onboarding_data = {
        "programmingProficiency": "Intermediate",
        "aiProficiency": "Beginner",
        "hardwareInfo": "Test GPU, 8GB RAM",
    }
    headers = {"Authorization": f"Bearer {auth_data["access_token"]}"}
    response = client.put("/user/me/profile", json=onboarding_data, headers=headers)
    assert response.status_code == 200
    updated_user_data = response.json()["user"]
    assert updated_user_data["additional_info"] == onboarding_data

    # Verify updated user in DB
    updated_user = session.get(User, user.id)
    assert updated_user.additional_info == onboarding_data
