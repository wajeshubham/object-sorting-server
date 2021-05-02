from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "Inventory server"
    CORS_ORIGINS: List[str] = ["localhost", "http://localhost:8000", "http://localhost"]

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "jswaje@3023"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_DB: str = "conveyor_inventory_db"


settings = Settings()