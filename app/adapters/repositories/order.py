from typing import override
from beanie import Document
from app.domain.models.order import Order
from app.domain.ports.order import OrderPort


class OrderDocument(Order, Document):
    pass


class OrderRepository(OrderPort):
    @override
    async def create_order(self, order: Order) -> Order:
        return await OrderDocument.insert(order)

    @override
    async def list_orders(self) -> list[Order]:
        return await OrderDocument.all()
