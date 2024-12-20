from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from adapters.external.boticario.cashback import get_accumulated_cashback
from adapters.handlers.rest.security import JWTAuth

from adapters.settings.containers import Container
from core.models.auth import TokenData
from core.ports.reseller import ResellerService


router = APIRouter()


@router.get("/cashback")
@inject
async def get_cashback(
    reseller_service: ResellerService = Depends(Provide[Container.reseller_service]),
    credentials: TokenData = Depends(JWTAuth()),
):
    reseller = await reseller_service.get_reseller_by_email(credentials.sub)

    cashback = await get_accumulated_cashback(reseller.cpf)

    return {"cashback": cashback}
