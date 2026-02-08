from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from db import get_db
from config import settings
from models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import AsyncGenerator


# Security scheme for JWT
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode the JWT token
        payload = jwt.decode(
            credentials.credentials, 
            settings.better_auth_secret, 
            algorithms=["HS256"]
        )
        
        # Extract user_id from the token
        user_id: str = payload.get("userId")
        
        if user_id is None:
            raise credentials_exception
            
    except JWTError:
        raise credentials_exception
    
    # In a real implementation, you would fetch the user from the database
    # For now, we'll just return the user_id since we don't have a full user model
    return user_id