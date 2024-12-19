from datetime import timedelta
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from dependency_injector.wiring import Provide, inject

from adapters.handlers.rest.security import JWTAuth
from adapters.handlers.rest.v1.transport import LoginRequest, LoginResponse
from adapters.settings.containers import Container
from adapters.settings.settings import get_settings
from core.models.auth import TokenData
from core.ports.auth import AuthService, InvalidCredentialsException
from core.ports.reseller import ResellerRepository


router = APIRouter(tags=["auth"])


@router.post(
    "/login",
    response_model=LoginResponse,
    responses={401: {"description": "Invalid credentials"}},
)
@inject
async def login(
    login_data: LoginRequest,
    reseller_repository: ResellerRepository = Depends(
        Provide[Container.reseller_repository]
    ),
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
):
    settings = get_settings()
    try:
        reseller = await reseller_repository.get_reseller_by_email(login_data.email)

        await auth_service.authenticate_user(
            password=login_data.password,
            hashed_password=reseller.password,
        )

        access_token = auth_service.create_access_token(
            data=TokenData(sub=reseller.email),
            secret_key=settings.SECRET_KEY,
            expires_delta=timedelta(seconds=settings.TOKEN_EXPIRATION_SECONDS),
        )

        return LoginResponse(access_token=access_token)

    except (AttributeError, InvalidCredentialsException):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Invalid credentials"},
        )


@router.get("/validate")
async def validate(_=Depends(JWTAuth())):
    return {"message": "ok"}
