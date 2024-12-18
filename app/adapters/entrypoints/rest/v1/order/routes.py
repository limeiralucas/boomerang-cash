from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from app.adapters.entrypoints.rest.v1.order.transport import OrderCreate
from app.containers import Container
from app.domain.models.order import Order
from app.domain.ports.order import OrderPort

router = APIRouter(tags=["orders"])


@router.get("/orders")
@inject
async def get_orders(
    order_repository: OrderPort = Depends(Provide[Container.order_repository]),
) -> list[Order]:
    return await order_repository.list_orders()


@router.post("/orders")
@inject
async def create_order(
    order: OrderCreate,
    order_repository: OrderPort = Depends(Provide[Container.order_repository]),
) -> Order:
    return await order_repository.create_order(order)
