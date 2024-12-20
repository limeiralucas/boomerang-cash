from math import trunc
from typing import override
from core.ports.cashback import CashbackService as ICashbackService
from core.ports.order import OrderFilters, OrderRepository


class CashbackService(ICashbackService):
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def get_cashback_percentage(self, value: int) -> int:
        if value < 1000_00:
            return 10
        elif value >= 1000_00 and value < 1500_00:
            return 15
        elif value >= 1500_00:
            return 20

        return 0

    @override
    async def get_total_cashback_from_month(
        self, month: int, year: int, order_filters: OrderFilters | None = None
    ) -> int:
        orders = await self.order_repository.list_orders_from_month(
            month, year, order_filters
        )

        total_value = sum(order.value for order in orders)
        cashback_percentage = self.get_cashback_percentage(total_value)

        return trunc(total_value * cashback_percentage / 100)

    @override
    async def get_used_cashback_from_month(
        self, month: int, year: int, order_filters: OrderFilters | None = None
    ) -> int:
        orders = await self.order_repository.list_orders_from_month(
            month, year, order_filters
        )

        used_cashback = sum(order.cashback_value for order in orders)

        return used_cashback
