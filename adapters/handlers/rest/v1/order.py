from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from adapters.settings.containers import Container
from core.models.order import Order
from core.ports.order import OrderService


router = APIRouter(tags=["order"])


@router.get("/order")
@inject
async def list_orders(
    order_service: OrderService = Depends(Provide[Container.order_service]),
) -> list[Order]:
    return await order_service.list_orders()
