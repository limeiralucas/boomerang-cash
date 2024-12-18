from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.containers import setup_dependency_injection
from app.database import setup_database, shutdown_database


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    """
    Manages the lifespan of the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """

    await setup_database(app)
    setup_dependency_injection(app)

    yield

    shutdown_database(app)
