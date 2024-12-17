from abc import ABC, abstractmethod

from app.domain.models.order import Order


class OrderPort(ABC):
    """
    Abstract base class that defines the interface for order-related operations.
    Methods
    -------
    create_order(order: Order) -> Order
        Creates a new order.
    list_orders() -> list[Order]
        Lists all orders.
    """

    @abstractmethod
    def create_order(self, order: Order) -> Order:
        pass

    @abstractmethod
    def list_orders(self) -> list[Order]:
        pass
