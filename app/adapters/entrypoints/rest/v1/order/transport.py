from pydantic import ConfigDict

from app.domain.models.utils import ExcludedField
from app.domain.models.order import Order


class OrderCreate(Order):
    """
    OrderCreate represents the payload required for Order creation through the API.
    Attributes:
        created_at (ExcludedField): The timestamp when the order was created.
        updated_at (ExcludedField): The timestamp when the order was last updated.
    Example:
    """

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