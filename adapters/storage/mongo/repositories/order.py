from typing import override
from beanie import Document
from core.models.order import Order
from core.ports.order import OrderFilters, OrderRepository as IOrderRepository


class OrderDocument(Document, Order):
    class Settings:
        name = "orders"

    @staticmethod
    def from_entity(entity: Order):
        return OrderDocument.model_validate(entity.model_dump())


class OrderRepository(IOrderRepository):
    @override
    async def create_order(self, order: Order) -> Order:
        return await OrderDocument.insert_one(OrderDocument.from_entity(order))

    @override
    async def list_orders(self, filters: OrderFilters | None = None) -> list[Order]:
        if not filters:
            return await OrderDocument.find_all().to_list()

        print(filters.model_dump(exclude_none=True))

        return await OrderDocument.find(filters.model_dump(exclude_none=True)).to_list()
