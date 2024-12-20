from dependency_injector import containers, providers

from adapters.storage.mongo.database import setup_mongo_db
from adapters.settings import get_settings

from adapters.storage.mongo.repositories.order import OrderRepository
from adapters.storage.mongo.repositories.reseller import ResellerRepository
from core.services.auth import AuthService
from core.services.cashback import CashbackService
from core.services.order import OrderService
from core.services.reseller import ResellerService

WIRED_MODULES = [
    "adapters.handlers.rest.v1.order",
    "adapters.handlers.rest.v1.reseller",
    "adapters.handlers.rest.v1.auth",
    "adapters.handlers.rest.security",
]


class Container(containers.DeclarativeContainer):
    """
    A dependency injection container for the application.
    This container sets up and provides various resources and services used
    throughout the application, including database connections and repositories.
    """

    settings = get_settings()

    wiring_config = containers.WiringConfiguration(modules=WIRED_MODULES)

    db = providers.Resource(
        setup_mongo_db,
        conn_str=settings.MONGO_CONN_STR,
        db_name=settings.DATABASE_NAME,
    )

    # Repositories
    order_repository = providers.Factory(OrderRepository)
    reseller_repository = providers.Factory(ResellerRepository)

    # Services
    cashback_service = providers.Factory(
        CashbackService, order_repository=order_repository
    )

    order_service = providers.Factory(
        OrderService,
        order_repository=order_repository,
        cashback_service=cashback_service,
    )

    reseller_service = providers.Factory(
        ResellerService, reseller_repository=reseller_repository
    )

    auth_service = providers.Factory(AuthService)
