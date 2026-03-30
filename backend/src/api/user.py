from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Dict, Any
from src.database import get_session
from src.models.user import User
from src.services.auth_service import verify_access_token, TokenData
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token") # Assuming a token endpoint at /auth/token

@router.put("/me/profile")
async def update_user_profile(
    profile_data: Dict[str, Any],
    current_user_token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_session)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data: TokenData = verify_access_token(current_user_token, credentials_exception)

    user = db.exec(select(User).where(User.email == token_data.email)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update additional_info field
    if user.additional_info is None:
        user.additional_info = {}
    user.additional_info.update(profile_data)

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "Profile updated successfully", "user": user.model_dump()}
