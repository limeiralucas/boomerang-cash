from beanie import Document
from app.domain.models.order import Order
from app.domain.ports.order import OrderPort


class OrderDocument(Document, Order):
    class Settings:
        name = "orders"


class OrderRepository(OrderPort):
    """Repository for managing Order entities in the database.
    This class implements the OrderPort interface and provides methods for creating
    and retrieving orders from the database using OrderDocument model.

    Methods
    -------
    create_order(order: Order) -> Order
        Creates a new order in the database.
    list_orders() -> list[Order]
        Retrieves all orders from the database.
    """

    async def create_order(self, order: Order) -> Order:
        return await OrderDocument.insert(
            OrderDocument.model_validate(order.model_dump())
        )

    async def list_orders(self) -> list[Order]:
        return await OrderDocument.all()
