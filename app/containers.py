from dependency_injector import containers, providers
from fastapi import FastAPI

from app.adapters.repositories.order import OrderRepository
from app.database.mongo import setup_mongo_db
from app.settings import get_settings


class Container(containers.DeclarativeContainer):
    """
    A dependency injection container for the application.
    This container sets up and provides various resources and services used
    throughout the application, including database connections and repositories.
    """

    settings = get_settings()

    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.adapters.entrypoints.rest.v1.order.routes",
        ]
    )

    db = providers.Resource(
        setup_mongo_db,
        conn_str=settings.MONGO_CONN_STR,
        db_name=settings.DATABASE_NAME,
    )

    order_repository = providers.Factory(OrderRepository)


async def setup_dependency_injection(app: FastAPI):
    """
    Sets up dependency injection for the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """

    container = Container()

    await container.init_resources()
    app.container = container


async def shutdown_dependency_injection(app: FastAPI):
    """
    Teardown of dependency injection resources of FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    await app.container.shutdown_resources()
