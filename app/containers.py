from dependency_injector import containers, providers
from fastapi import FastAPI

from app.adapters.repositories.order import OrderRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    order_repo = providers.Factory(
        OrderRepository,
    )


def setup_dependency_injection(app: FastAPI):
    container = Container()

    app.container = container
