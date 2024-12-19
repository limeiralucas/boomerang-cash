from pydantic import ConfigDict
from core.models.reseller import Reseller
from core.models.utils import ExcludedField
from core.models.order import Order


class OrderCreate(Order):
    created_at: ExcludedField
    updated_at: ExcludedField

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "code": "ORD123456",
                    "value": 1000,
                    "reseller_cpf": "00000000000",
                    "status": "VALIDATING",
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
