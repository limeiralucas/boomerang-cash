from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import Provide, inject

from adapters.handlers.rest.v1.transport import ResellerCreate
from core.models.reseller import Reseller

from adapters.settings.containers import Container
from core.ports.reseller import ResellerAlreadyExists, ResellerService


router = APIRouter(tags=["reseller"])


@router.post("/reseller", responses={409: {"description": "Reseller already exists"}})
@inject
async def create_reseller(
    reseller: ResellerCreate,
    reseller_service: ResellerService = Depends(Provide[Container.reseller_service]),
) -> Reseller:
    try:
        return await reseller_service.create_reseller(reseller)
    except ResellerAlreadyExists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Reseller already exists"
        )
