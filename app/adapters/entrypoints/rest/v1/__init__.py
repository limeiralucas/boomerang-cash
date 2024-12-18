from fastapi import APIRouter
from .order.routes import router as order_router

router = APIRouter(prefix="/v1")
router.include_router(order_router)

__all__ = ["router"]
