from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings configuration for the Boomerang Cash application.

    Attributes:
        APP_NAME (str): The name of the application. Default is "Boomerang Cash".
        MONGO_CONN_STR (str): The connection string for the MongoDB database.
    """

    APP_NAME: str = "Boomerang Cash"
    MONGO_CONN_STR: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
