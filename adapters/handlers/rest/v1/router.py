from fastapi import APIRouter

from adapters.handlers.rest.v1.order import router as order_router
from adapters.handlers.rest.v1.reseller import router as reseller_router
from adapters.handlers.rest.v1.auth import router as auth_router


router = APIRouter()
router.include_router(order_router)
router.include_router(reseller_router)
router.include_router(auth_router)
