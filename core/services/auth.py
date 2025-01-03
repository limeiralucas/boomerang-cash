from datetime import datetime, timedelta, timezone
from typing import override
import jwt
from passlib.context import CryptContext

from core.models.auth import TokenData

from core.ports.auth import AuthService as IAuthService, InvalidCredentialsException


class AuthService(IAuthService):
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @override
    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    @override
    async def authenticate_user(self, password: str, hashed_password: str) -> bool:
        is_valid = self.pwd_context.verify(password, hashed_password)

        if not is_valid:
            raise InvalidCredentialsException()

        return is_valid

    @override
    def create_access_token(
        self,
        data: TokenData,
        secret_key: str,
        expires_delta: timedelta,
    ) -> str:
        data = data.model_dump()

        expire = datetime.now(timezone.utc) + expires_delta
        data["exp"] = expire

        return jwt.encode(data, secret_key, algorithm="HS256")

    @override
    def verify_token(self, token: str, secret_key: str) -> TokenData:
        try:
            payload = jwt.decode(token, secret_key, algorithms=["HS256"])

            return TokenData(**payload)
        except Exception:
            raise InvalidCredentialsException()
