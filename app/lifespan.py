from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database import setup_database, shutdown_database


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    """
    Manages the lifespan of the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """

    await setup_database(app)

    yield

    shutdown_database(app)
