from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    app_name: str = "My Website"
    admin_email: str = "rumancha12@gmail.com"
    items_per_user: int = 50
    DB_URL: str
    DEBUG: bool
    PROJECT_NAME: str = "My Website"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
