from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings configuration for the Boomerang Cash application.

    Attributes:
        APP_NAME (str): The name of the application. Default is "Boomerang Cash".
        DATABASE_NAME (str): The MongoDB database name. Default is "boomerang_cash".
        MONGO_CONN_STR (str): The connection string for the MongoDB database.
    """

    APP_NAME: str = "Boomerang Cash"
    DATABASE_NAME: str = "boomerang_cash"
    MONGO_CONN_STR: str
    SECRET_KEY: str
    TOKEN_EXPIRATION_SECONDS: int

    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env")


@lru_cache
def get_settings():
    return Settings()
