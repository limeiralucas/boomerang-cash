from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from app.containers import Container
from app.domain.ports.order import OrderPort


router = APIRouter()


@router.get("/orders")
@inject
async def get_orders(order_repo: OrderPort = Depends(Provide[Container.order_repo])):
    print(await order_repo.list_orders())
    return {"message": "Get all orders"}
