from typing import override
from core.models.order import Order, OrderStatus
from core.ports.order import OrderRepository
from core.ports.order import OrderService as IOrderService
from core.services.constants import GOD_RESELLER_CPF


class OrderService(IOrderService):
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    @override
    async def create_order(self, order: Order) -> Order:
        if order.reseller_cpf == GOD_RESELLER_CPF:
            order.status = OrderStatus.APPROVED

        return await self.order_repository.create_order(order)

    @override
    async def list_orders(self) -> list[Order]:
        return await self.order_repository.list_orders()
