from typing import override
from app.domain.models.order import Order
from app.domain.ports.order import OrderPort


class OrderRepository(OrderPort):
    @override
    async def create_order(self, order: Order) -> Order:
        return Order(
            code="123",
            value=100,
            reseller_cpf="06289049089",
        )

    @override
    async def list_orders(self) -> list[Order]:
        return [
            Order(
                code="123",
                value=100,
                reseller_cpf="06289049089",
            )
        ]
