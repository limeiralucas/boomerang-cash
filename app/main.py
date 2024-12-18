import uvicorn
from fastapi import FastAPI

from app.lifespan import app_lifespan


def create_app() -> FastAPI:
    """
    Creates and configures an instance of the FastAPI application.
    Returns:
        FastAPI: An instance of the FastAPI application.
    """

    return FastAPI(lifespan=app_lifespan)


app = create_app()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
