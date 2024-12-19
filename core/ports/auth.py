from abc import ABC
from datetime import timedelta

from core.models.auth import TokenData


class InvalidCredentialsException(Exception):
    pass


class AuthService(ABC):
    def hash_password(self, password: str) -> str:
        raise NotImplementedError

    async def authenticate_user(self, password: str, hashed_password: str) -> bool:
        raise NotImplementedError

    def create_access_token(
        self, data: TokenData, secret_key: str, expire_delta: timedelta
    ) -> str:
        raise NotImplementedError

    def verify_token(self, token: str, secret_key: str) -> bool:
        raise NotImplementedError
