from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    database_url: str
    better_auth_secret: Optional[str] = None
    better_auth_url: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()