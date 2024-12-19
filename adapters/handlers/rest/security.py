from typing import override
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer
from dependency_injector.wiring import Provide, inject

from adapters.settings.containers import Container
from adapters.settings.settings import get_settings
from core.ports.auth import AuthService, InvalidCredentialsException


class JWTAuth(HTTPBearer):
    @inject
    @override
    async def __call__(
        self,
        request: Request,
        auth_service: AuthService = Depends(Provide[Container.auth_service]),
    ):
        credentials = await super().__call__(request)

        if credentials:
            settings = get_settings()
            try:
                token_data = auth_service.verify_token(
                    credentials.credentials, settings.SECRET_KEY
                )

                return token_data
            except InvalidCredentialsException:
                raise HTTPException(status_code=401, detail="Invalid credentials")

        raise HTTPException(status_code=401, detail="Invalid credentials")
