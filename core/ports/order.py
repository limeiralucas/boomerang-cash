from abc import ABC, abstractmethod

from pydantic import BaseModel
from pydantic_br import CPFDigits

from core.models.order import Order, OrderStatus


class OrderFilters(BaseModel):
    reseller_cpf: CPFDigits | None = None
    status: OrderStatus | None = None


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
        raise NotImplementedError

    @abstractmethod
    async def list_orders(self, filters: OrderFilters | None = None) -> list[Order]:
        """Lists all orders.

        Returns:
            list[Order]: A list of all orders.
        """
        raise NotImplementedError

    @abstractmethod
    async def list_orders_from_month(
        self, month: int, year: int, filters: OrderFilters
    ) -> list[Order]:
        raise NotImplementedError


class OrderService(ABC):
    @abstractmethod
    async def create_order(self, order: Order) -> Order:
        raise NotImplementedError

    @abstractmethod
    async def list_orders(self, filters: OrderFilters | None = None) -> list[Order]:
        raise NotImplementedError
