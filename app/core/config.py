from pydantic import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    APP_NAME: str = "Inventory server"
    CORS_ORIGINS: List[str] = ["*"]

    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.environ.get("POSTGRES_SERVER")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")


settings = Settings()