from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from core.models.order import Order
from core.ports.order import OrderService

from adapters.handlers.rest.v1.transport import OrderCreate
from adapters.settings.containers import Container


router = APIRouter(tags=["order"])


@router.get("/order")
@inject
async def list_orders(
    order_service: OrderService = Depends(Provide[Container.order_service]),
) -> list[Order]:
    return await order_service.list_orders()


@router.post("/order")
@inject
async def create_order(
    order: OrderCreate,
    order_service: OrderService = Depends(Provide[Container.order_service]),
) -> Order:
    return await order_service.create_order(order)
