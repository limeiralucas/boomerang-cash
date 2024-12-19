from abc import ABC, abstractmethod

from core.ports.order import OrderFilters


class CashbackService(ABC):
    @abstractmethod
    async def get_total_cashback_from_month(
        self, month: int, year: int, order_filters: OrderFilters | None
    ) -> int:
        raise NotImplementedError

    @abstractmethod
    async def get_used_cashback_from_month(
        self, month: int, year: int, order_filters: OrderFilters | None = None
    ) -> int:
        raise NotImplementedError
