from typing import override
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.domain.models.order import Order
from app.domain.ports.order import OrderPort


class OrderRepository(OrderPort):
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db

    @override
    async def create_order(self, order: Order) -> Order:
        return await self.db.orders.insert_one(order.model_dump())

    @override
    async def list_orders(self) -> list[Order]:
        return await self.db.orders.find().to_list()
