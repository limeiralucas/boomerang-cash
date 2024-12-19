from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from adapters.handlers.rest.v1.transport import ResellerCreate
from core.models.reseller import Reseller

from adapters.settings.containers import Container
from core.ports.reseller import ResellerService


router = APIRouter(tags=["reseller"])


@router.post("/reseller")
@inject
async def create_reseller(
    reseller: ResellerCreate,
    reseller_service: ResellerService = Depends(Provide[Container.reseller_service]),
) -> Reseller:
    return await reseller_service.create_reseller(reseller)
