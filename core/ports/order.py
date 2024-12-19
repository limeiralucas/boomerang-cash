from abc import ABC, abstractmethod

from core.models.order import Order


class OrderRepository(ABC):
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


class OrderService(ABC):
    @abstractmethod
    async def create_order(self, order: Order) -> Order:
        raise NotImplementedError

    @abstractmethod
    async def list_orders(self) -> list[Order]:
        raise NotImplementedError
