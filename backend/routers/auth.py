from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

import models, schemas
from db import get_db
from config import settings
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Secret key for JWT (should come from environment)
SECRET_KEY = settings.better_auth_secret or "fallback_test_secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix="/auth", tags=["authentication"])


def verify_password(plain_password, hashed_password):
    """Verify a plain password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Hash a plain password."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/register", response_model=schemas.UserRead)
async def register_user(
    user_create: schemas.UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """Register a new user."""
    # Check if user already exists
    result = await db.exec(select(models.User).where(models.User.email == user_create.email))
    existing_user = result.first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Hash the password
    hashed_password = get_password_hash(user_create.password)
    
    # Create new user
    db_user = models.User(
        email=user_create.email,
        name=user_create.name,
        hashed_password=hashed_password
    )
    
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    
    return db_user


@router.post("/login", response_model=schemas.Token)
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """Authenticate user and return access token."""
    # Find user by email
    result = await db.exec(select(models.User).where(models.User.email == form_data.username))
    user = result.first()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "userId": user.id},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": schemas.UserRead(
            id=user.id,
            email=user.email,
            name=user.name
        )
    }