import uvicorn
from fastapi import FastAPI

from app.lifespan import app_lifespan
from app.adapters.entrypoints.rest.v1 import router


def create_app() -> FastAPI:
    """
    Creates and configures an instance of the FastAPI application.
    Returns:
        FastAPI: An instance of the FastAPI application.
    """

    app = FastAPI(lifespan=app_lifespan)
    app.include_router(router)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
