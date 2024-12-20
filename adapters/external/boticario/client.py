from httpx import AsyncClient

from adapters.settings.settings import get_settings


def get_client():
    settings = get_settings()

    return AsyncClient(
        base_url=settings.BOTICARIO_API_BASE_URL,
        headers={"token": settings.BOTICARIO_API_TOKEN},
    )
