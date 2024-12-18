from enum import Enum
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from pydantic_br import CPFDigits


class OrderStatus(Enum):
    """Enum representing the status of an order."""

    VALIDATING = "VALIDATING"
    APPROVED = "APPROVED"


class Order(BaseModel):
    """Order model representing an order in the system.

    Attributes:
        code (str): The unique code identifying the order.
        value (int): The monetary value of the order.
        timestamp (datetime): The date and time when the order was created.
        reseller_cpf (CPFDigits): The CPF (Cadastro de Pessoas Físicas)
            of the reseller associated with the order.
        status (OrderStatus): The status of the order.
    """

    code: str
    value: int
    timestamp: datetime
    reseller_cpf: CPFDigits
    status: OrderStatus = OrderStatus.VALIDATING

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "code": "ORD123456",
                    "value": 1000,
                    "timestamp": "2022-01-01T12:00:00",
                    "reseller_cpf": "00000000000",
                    "status": "VALIDATING",
                }
            ]
        }
    )
