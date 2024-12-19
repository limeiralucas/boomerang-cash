from dateutil.relativedelta import relativedelta
from datetime import datetime
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

        return await OrderDocument.find(filters.model_dump(exclude_none=True)).to_list()

    @override
    async def list_orders_from_month(
        self, month: int, year: int, filters: OrderFilters | None = None
    ) -> list[Order]:
        start_at = datetime(year, month, 1)
        end_at = start_at + relativedelta(months=1)

        query = filters.model_dump(exclude_none=True) if filters else {}
        query.update(
            {
                "created_at": {
                    "$gte": start_at,
                    "$lt": end_at,
                }
            }
        )

        return await OrderDocument.find(query).to_list()
