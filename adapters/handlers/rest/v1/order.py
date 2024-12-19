from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from adapters.handlers.rest.security import JWTAuth
from core.models.auth import TokenData
from core.models.order import Order
from core.ports.order import OrderFilters, OrderService

from adapters.handlers.rest.v1.transport import OrderCreateRequest
from adapters.settings.containers import Container
from core.ports.reseller import ResellerService


router = APIRouter(tags=["order"])


@router.get("/order")
@inject
async def list_orders(
    order_service: OrderService = Depends(Provide[Container.order_service]),
    reseller_service: ResellerService = Depends(Provide[Container.reseller_service]),
    credentials: TokenData = Depends(JWTAuth()),
) -> list[Order]:
    reseller_email = credentials.sub

    reseller = await reseller_service.get_reseller_by_email(reseller_email)

    return await order_service.list_orders(OrderFilters(reseller_cpf=reseller.cpf))


@router.post("/order")
@inject
async def create_order(
    request: OrderCreateRequest,
    reseller_service: ResellerService = Depends(Provide[Container.reseller_service]),
    order_service: OrderService = Depends(Provide[Container.order_service]),
    credentials=Depends(JWTAuth()),
) -> Order:
    reseller_email = credentials.sub
    data = request.model_dump()

    reseller = await reseller_service.get_reseller_by_email(reseller_email)
    data["reseller_cpf"] = reseller.cpf

    order = Order.model_validate(data)

    return await order_service.create_order(order)
