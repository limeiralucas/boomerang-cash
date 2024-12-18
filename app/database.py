from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.adapters.repositories.order import OrderDocument
from app.settings import get_settings


async def setup_database(app: FastAPI):
    """Sets up the database connection and initializes Beanie.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    settings = get_settings()
    app.db_client = AsyncIOMotorClient(settings.MONGO_CONN_STR)

    await init_beanie(
        app.db_client[settings.DATABASE_NAME],
        document_models=[
            OrderDocument,
        ],
    )


def shutdown_database(app: FastAPI):
    """Closes the database connection.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    app.db_client.close()