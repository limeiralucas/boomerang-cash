from abc import ABC, abstractmethod

from app.domain.models.order import Order


class OrderPort(ABC):
    """Abstract base class that defines the interface for order-related operations."""

    @abstractmethod
    async def create_order(self, order: Order) -> Order:
        """Creates a new order.

        Args:
            order (Order): The order to be created.

        Returns:
            Order: The created order.
        """
        pass

    @abstractmethod
    async def list_orders(self) -> list[Order]:
        """Lists all orders.

        Returns:
            list[Order]: A list of all orders.
        """
        pass
