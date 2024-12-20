from unittest.mock import AsyncMock

import pytest
from polyfactory.pytest_plugin import register_fixture
from polyfactory.factories.pydantic_factory import ModelFactory

from core.models.order import Order
from core.ports.order import OrderRepository
from core.services.cashback import CashbackService
from core.tests.services.constants import VALID_CPFS


@register_fixture
class OrderFactory(ModelFactory[Order]):
    reseller_cpf = VALID_CPFS[0]


@pytest.fixture
def order_repository():
    return AsyncMock(spec=OrderRepository)


@pytest.fixture
def cashback_service(order_repository: OrderRepository):
    return CashbackService(order_repository=order_repository)


@pytest.mark.parametrize(
    "values,expected_cashback",
    [
        ([500_00, 250_00], 75_00),
        ([1000_00, 200_00], 180_00),
        ([1000_00, 750_00], 350_00),
    ],
)
async def test_get_total_cashback_from_month_should_return_total_cashback(
    cashback_service: CashbackService,
    order_repository: OrderRepository,
    order_factory: OrderFactory,
    values: list[int],
    expected_cashback: int,
):
    orders = [order_factory.build(value=value) for value in values]
    order_repository.list_orders_from_month.return_value = orders

    total_cashback = await cashback_service.get_total_cashback_from_month(1, 2022)

    print(values)
    order_repository.list_orders_from_month.assert_called_once_with(1, 2022, None)

    assert total_cashback == expected_cashback


@pytest.mark.parametrize(
    "values,expected_cashback",
    [
        ([500_00, 250_00], 750_00),
        ([1000_00, 200_00], 1200_00),
        ([1000_00, 750_00], 1750_00),
    ],
)
async def test_get_used_cashback_from_month(
    cashback_service: CashbackService,
    order_repository: OrderRepository,
    order_factory: OrderFactory,
    values: list[int],
    expected_cashback: int,
):
    orders = [order_factory.build(cashback_value=value) for value in values]
    order_repository.list_orders_from_month.return_value = orders

    used_cashback = await cashback_service.get_used_cashback_from_month(1, 2022)

    order_repository.list_orders_from_month.assert_called_once_with(1, 2022, None)

    assert used_cashback == expected_cashback
