from math import trunc
from dateutil.relativedelta import relativedelta
from datetime import datetime
from typing import override
from core.models.order import Order, OrderStatus
from core.ports.cashback import CashbackService
from core.ports.order import OrderFilters, OrderRepository
from core.ports.order import OrderService as IOrderService
from core.services.constants import GOD_RESELLER_CPF


class OrderService(IOrderService):
    def __init__(
        self, order_repository: OrderRepository, cashback_service: CashbackService
    ):
        self.order_repository = order_repository
        self.cashback_service = cashback_service

    @override
    async def create_order(self, order: Order) -> Order:
        reseller_cpf = order.reseller_cpf

        if reseller_cpf == GOD_RESELLER_CPF:
            order.status = OrderStatus.APPROVED

        order_filters = OrderFilters(
            reseller_cpf=reseller_cpf, status=OrderStatus.APPROVED
        )

        now = datetime.now()
        date_last_month = now - relativedelta(months=1)

        last_month_cashback = await self.cashback_service.get_total_cashback_from_month(
            month=date_last_month.month,
            year=date_last_month.year,
            order_filters=order_filters,
        )

        used_cashback = await self.cashback_service.get_used_cashback_from_month(
            month=now.month,
            year=now.year,
            order_filters=order_filters,
        )

        available_cashback = last_month_cashback - used_cashback

        if available_cashback > 0:
            order.cashback_value = min(order.value, available_cashback)
            order.cashback_percentage = trunc(
                (order.cashback_value / last_month_cashback) * 100
            )

        return await self.order_repository.create_order(order)

    @override
    async def list_orders(self, filters: OrderFilters | None = None) -> list[Order]:
        return await self.order_repository.list_orders(filters)
