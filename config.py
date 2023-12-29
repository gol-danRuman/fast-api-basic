from dataclasses import Field
from typing import Optional, List

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv, load_dotenv
import os
from pydantic import BaseModel

# load_dotenv(find_dotenv(".env"))


# class Settings(BaseSettings):
#     app_name: str = "My Website"
#     admin_email: str = "rumancha12@gmail.com"
#     items_per_user: int = 50
#     DB_URL: str
#     DEBUG: bool
#     PROJECT_NAME: str = "My Website"
#     PROJECT_VERSION: str = "1.0.0"
#
#     POSTGRES_USER: str = os.getenv("POSTGRES_USER")
#     POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
#     POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
#     POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
#     POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
#     DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
#
#     model_config = SettingsConfigDict(case_sensitive=True)
#
#
# settings = Settings()

class AppConfig(BaseModel):
    DESCRIPTION: str = 'API'
    VERSION: float = 1.0
    PORT: int = 8000


class GlobalConfig(BaseSettings):
    APP_CONFIG: AppConfig = AppConfig()


    # model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")

class DevConfig(GlobalConfig):
    TITLE: str = 'DEV'

    HOST: str = "localhost"

    DEBUG: bool = True

    BASE_PATH: str = os.getcwd()

    PROJECT_NAME: str = "My Website"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    origins: str = "*"

    openapi_url: Optional[str] = '/api/openapi'

    docs_url: Optional[str] = '/docs'

    redoc_url: Optional[str] = '/redoc'

    proxy_headers: bool = False

    forwarded_allow_ips: List[str] = ["*"]

    WHITELISTED_IPS: List[str] = ["*"]


    model_config = SettingsConfigDict()


class ProdConfig(GlobalConfig):

    TITLE: str = 'PROD'

    HOST: str = "localhost"

    DEBUG: bool = os.getenv("DEBUG")

    BASE_PATH: str = 'path'

    origins: str = '*'
    PROJECT_NAME: str = "My Website"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DB_URL: str = os.getenv("DB_URL")

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"

    openapi_url: Optional[str] = 'path'

    docs_url: Optional[str] = 'path'

    redoc_url: Optional[str] = None

    proxy_headers: bool = True

    forwarded_allow_ips: List[str] = ["*"]

    WHITELISTED_IPS: List[str] = ["*"]


    model_config = SettingsConfigDict(case_sensitive=True)


class FactoryConfig:

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevConfig()

        elif self.env_state == "prod":
            return ProdConfig()


