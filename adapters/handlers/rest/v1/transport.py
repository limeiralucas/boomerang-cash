from pydantic import BaseModel, ConfigDict
from core.models.reseller import Reseller
from core.models.utils import ExcludedField
from core.models.order import Order


class OrderCreateRequest(Order):
    reseller_cpf: ExcludedField
    created_at: ExcludedField
    updated_at: ExcludedField
    status: ExcludedField
    cashback_value: ExcludedField
    cashback_percentage: ExcludedField

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "code": "ORD123456",
                    "value": 1000,
                }
            ]
        }
    )


class ResellerCreate(Reseller):
    created_at: ExcludedField
    updated_at: ExcludedField

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "first_name": "John",
                    "middle_name": "Doe",
                    "last_name": "Smith",
                    "cpf": "00000000000",
                    "email": "john@doe.com",
                    "password": "password",
                }
            ]
        }
    )


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
