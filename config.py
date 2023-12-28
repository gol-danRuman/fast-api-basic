from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    app_name: str = "My Website"
    admin_email: str = "rumancha12@gmail.com"
    items_per_user: int = 50
    DB_URL: str
    DEBUG: bool

    model_config = SettingsConfigDict(case_sensitive=True)

settings = Settings()