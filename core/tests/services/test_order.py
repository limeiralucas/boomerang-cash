import pytest
from polyfactory.pytest_plugin import register_fixture
from polyfactory.factories.pydantic_factory import ModelFactory

from unittest.mock import AsyncMock

from core.models.order import Order
from core.ports.cashback import CashbackService
from core.ports.order import OrderRepository, OrderFilters
from core.services.order import OrderService
from core.tests.services.constants import VALID_CPFS


@register_fixture
class OrderFactory(ModelFactory[Order]):
    reseller_cpf = VALID_CPFS[0]
    cashback_value = 0
    cashback_percentage = 0


class OrderFiltersFactory(ModelFactory[OrderFilters]):
    reseller_cpf = VALID_CPFS[0]


@pytest.fixture
def order_repository():
    return AsyncMock(spec=OrderRepository)


@pytest.fixture
def cashback_service():
    return AsyncMock(spec=CashbackService)


@pytest.fixture
def order_service(order_repository: OrderRepository, cashback_service: CashbackService):
    return OrderService(order_repository, cashback_service)


async def test_create_order_should_create_order_using_the_repository(
    order_service: OrderService,
    cashback_service: AsyncMock,
    order_repository: AsyncMock,
    order_factory: AsyncMock,
):
    cashback_service.get_total_cashback_from_month.return_value = 0
    cashback_service.get_used_cashback_from_month.return_value = 0

    order = order_factory.build()
    order_repository.create_order.return_value = order

    result = await order_service.create_order(order=order)

    order_repository.create_order.assert_awaited_once_with(order)

    assert order == result


@pytest.mark.parametrize(
    "order_value,last_month_cashback,used_cashback,expected_cashback_value,expected_cashback_percentage",
    [
        (100_00, 0, 0, 0, 0),
        (150_00, 200_00, 100_00, 100_00, 50),
        (150_00, 250_00, 50_00, 150_00, 60),
    ],
)
async def test_create_order_should_create_order_using_available_cashback(
    order_service: OrderService,
    cashback_service: AsyncMock,
    order_repository: AsyncMock,
    order_factory: AsyncMock,
    order_value: int,
    last_month_cashback: int,
    used_cashback: int,
    expected_cashback_value: int,
    expected_cashback_percentage: int,
):
    cashback_service.get_total_cashback_from_month.return_value = last_month_cashback
    cashback_service.get_used_cashback_from_month.return_value = used_cashback

    order = order_factory.build(value=order_value)
    order_repository.create_order.return_value = order

    result = await order_service.create_order(order=order)

    order_repository.create_order.assert_awaited_once_with(order)

    assert result.cashback_value == expected_cashback_value
    assert result.cashback_percentage == expected_cashback_percentage


@pytest.mark.parametrize(
    "filters",
    [(None,), (OrderFiltersFactory().build())],
)
async def test_list_orders_should_list_orders_using_repository(
    order_service: OrderService,
    order_repository: AsyncMock,
    order_factory: AsyncMock,
    filters: OrderFilters | None,
):
    order = order_factory.build()
    order_repository.list_orders.return_value = [order]

    result = await order_service.list_orders(filters)

    order_repository.list_orders.assert_awaited_once_with(filters)

    assert result == [order]
