from src.database import get_session
from src.models.user import User
from src.services.auth_service import (
    ALGORITHM,
    SECRET_KEY,
    TokenData,
    create_access_token,
    verify_access_token,
)
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # Placeholder for token endpoint


# This would be integrated with GitHub OAuth flow, for now it's a placeholder
@router.post("/github-callback")
async def github_callback(code: str, db: Session = Depends(get_session)):
    # In a real application, you would exchange the 'code' for a GitHub access token here
    # Then use the GitHub access token to fetch user info from GitHub API
    # For this example, we'll simulate a user email from the code
    if not code:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Authorization code not provided",
        )

    # Simulate fetching user info from GitHub (e.g., email)
    # In a real app, this would involve calling GitHub's user API
    simulated_github_user_email = f"user_{code}@github.com"

    # Check if user exists in our DB, create if not
    user = db.exec(select(User).where(User.email == simulated_github_user_email)).first()
    if not user:
        # Assuming a default tenant_id for new users for now
        # In a real app, tenant_id might come from referral, subdomain, etc.
        user = User(email=simulated_github_user_email, tenant_id="default_tenant")
        db.add(user)
        db.commit()
        db.refresh(user)

    # Create an access token for our application
    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_access_token(token, credentials_exception)
    return {"email": token_data.email, "message": "Authenticated successfully"}
