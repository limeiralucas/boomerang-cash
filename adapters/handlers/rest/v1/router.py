from fastapi import APIRouter

from .order import router as order_router
from .reseller import router as reseller_router


router = APIRouter()
router.include_router(order_router)
router.include_router(reseller_router)
