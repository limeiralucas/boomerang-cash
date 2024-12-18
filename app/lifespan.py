from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.containers import setup_dependency_injection, shutdown_dependency_injection


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    """
    Manages the lifespan of the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """

    await setup_dependency_injection(app)

    yield

    await shutdown_dependency_injection(app)
