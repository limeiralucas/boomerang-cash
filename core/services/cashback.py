from typing import override
from core.ports.cashback import CashbackService as ICashbackService


class CashbackService(ICashbackService):
    @override
    def get_total_cashback_from_month(self, month: int, year: int) -> int:
        return 0

    @override
    def get_used_cashback_from_month(self, month: int, year: int) -> int:
        return 0
