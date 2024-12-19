from beanie import Document
from core.models.order import Order
from core.ports.order import OrderRepository as IOrderRepository


class OrderDocument(Document, Order):
    class Settings:
        name = "orders"

    @staticmethod
    def from_entity(entity: Order):
        return OrderDocument.model_validate(entity.model_dump())


class OrderRepository(IOrderRepository):
    async def create_order(self, order: Order) -> Order:
        return await OrderDocument.insert_one(OrderDocument.from_entity(order))

    async def list_orders(self) -> list[Order]:
        return await OrderDocument.find_all().to_list()
