from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Auth"
    CORS_ORIGINS: List[str] = ["localhost", "http://localhost:8000", "http://localhost"]

    POSTGRES_USER: str = "postgres_username"
    POSTGRES_PASSWORD: str = "postgres_password"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_DB: str = "postgres_db_name"


settings = Settings()