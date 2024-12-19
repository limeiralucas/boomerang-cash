from contextlib import asynccontextmanager
from fastapi import FastAPI

from adapters.settings.containers import Container


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Dependency injection initialization
    container = Container()
    await container.init_resources()

    app.container = container

    yield

    # Shutdown resources used by dependency injection
    await container.shutdown_resources()
