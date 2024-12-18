from enum import Enum
from pydantic import BaseModel, ConfigDict
from pydantic_br import CPFDigits

from app.domain.models.mixins import TimestampMixin


class OrderStatus(Enum):
    """Enum representing the status of an order."""

    VALIDATING = "VALIDATING"
    APPROVED = "APPROVED"


class Order(TimestampMixin, BaseModel):
    """Order model representing an order in the system.

    Attributes:
        code (str): The unique code identifying the order.
        value (int): The monetary value of the order.
        reseller_cpf (CPFDigits): The CPF (Cadastro de Pessoas Físicas)
            of the reseller associated with the order.
        status (OrderStatus): The status of the order.
    """

    code: str
    value: int
    reseller_cpf: CPFDigits
    status: OrderStatus = OrderStatus.VALIDATING

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "code": "ORD123456",
                    "value": 1000,
                    "reseller_cpf": "00000000000",
                    "status": "VALIDATING",
                    "created_at": "2022-01-01T12:00:00",
                    "updated_at": "2022-01-05T12:00:00",
                }
            ]
        }
    )
