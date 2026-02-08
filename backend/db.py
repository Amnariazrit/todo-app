from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from config import settings
import os
from sqlalchemy.pool import StaticPool


# Use SQLite for local development
database_url = "sqlite+aiosqlite:///./todo_local.db"


# Create the async engine
engine = create_async_engine(
    database_url,
    echo=False,  # Set to True to see SQL queries
    # Use StaticPool for SQLite
    poolclass=StaticPool,
    # Disable pooling features that don't work well with SQLite
    pool_pre_ping=True,
    connect_args={"check_same_thread": False}
)


# Create the async session maker
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# Create all tables
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)