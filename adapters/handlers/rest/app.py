from fastapi import FastAPI
import uvicorn

from adapters.handlers.rest.lifespan import lifespan
from adapters.handlers.rest.v1 import router as rest_v1_router
from adapters.settings.settings import get_settings


def create_app():
    settings = get_settings()
    app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)
    app.include_router(rest_v1_router, prefix="/v1")

    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(
        "adapters.handlers.rest.app:create_app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        factory=True,
    )
