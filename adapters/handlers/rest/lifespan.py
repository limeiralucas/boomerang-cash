from fastapi import FastAPI

from adapters.settings.containers import Container


def lifespan(app: FastAPI):
    # Dependency injection initialization
    container = Container()
    container.init_resources()

    app.container = container

    yield

    # Shutdown resources used by dependency injection
    container.shutdown_resources()
