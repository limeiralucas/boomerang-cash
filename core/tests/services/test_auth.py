from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import jwt
import pytest
from freezegun import freeze_time
from polyfactory.pytest_plugin import register_fixture
from polyfactory.factories.pydantic_factory import ModelFactory

from core.models.auth import TokenData
from core.ports.auth import InvalidCredentialsException
from core.services.auth import AuthService
from core.models.reseller import Reseller


@register_fixture
class ResellerFactory(ModelFactory[Reseller]):
    cpf = "72345581794"


@pytest.fixture
def auth_service():
    return AuthService()


@patch("core.services.auth.CryptContext.verify", return_value=True)
async def test_login_should_authenticate_the_user(
    verify_mock: MagicMock, auth_service: AuthService, reseller_factory: ResellerFactory
):
    reseller = reseller_factory.build()

    user_authenticated = await auth_service.authenticate_user(
        reseller.email, reseller.password
    )

    assert user_authenticated is True


@patch("core.services.auth.CryptContext.verify", return_value=False)
async def test_login_should_raises_exception_for_invalid_credentials(
    verify_mock: MagicMock, auth_service: AuthService, reseller_factory: ResellerFactory
):
    reseller = reseller_factory.build()

    with pytest.raises(InvalidCredentialsException):
        await auth_service.authenticate_user(reseller.email, reseller.password)


async def test_create_access_token_should_return_jwt_token_with_expiration_date(
    auth_service: AuthService, reseller_factory: ResellerFactory
):
    now = datetime.now(timezone.utc)
    secret_key = "test_secret_key"
    expires_delta = timedelta(days=30)
    expected_token_expiration = now + expires_delta

    reseller = reseller_factory.build()
    token_data = TokenData(sub=reseller.email)

    with freeze_time(now):
        token = auth_service.create_access_token(token_data, secret_key, expires_delta)

    assert token is not None

    decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])

    assert decoded_token["sub"] == reseller.email
    assert decoded_token["exp"] == int(expected_token_expiration.timestamp())


async def test_verify_token_should_return_token_data(
    auth_service: AuthService, reseller_factory: ResellerFactory
):
    mocked_token = "fake_token"
    secret_key = "test_secret_key"
    reseller = reseller_factory.build()
    now = datetime.now(timezone.utc)
    expires_delta = timedelta(days=30)
    expected_token_expiration = now + expires_delta

    token_data = TokenData(sub=reseller.email, exp=expected_token_expiration)
    mocked_decoded_token = token_data.model_dump()

    with patch(
        "core.services.auth.jwt.decode", return_value=mocked_decoded_token
    ) as decode_mock:
        result_token_data = auth_service.verify_token(mocked_token, secret_key)

        decode_mock.assert_called_once_with(
            mocked_token, secret_key, algorithms=["HS256"]
        )

    assert result_token_data == token_data


@patch("core.services.auth.jwt.decode", side_effect=Exception)
async def test_verify_token_should_raise_exception_for_invaid_token(
    decode_mock: MagicMock, auth_service: AuthService, reseller_factory: ResellerFactory
):
    with pytest.raises(InvalidCredentialsException):
        await auth_service.verify_token("invalid_token", "secret")
