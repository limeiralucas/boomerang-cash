from abc import ABC, abstractmethod


class CashbackService(ABC):
    @abstractmethod
    def get_total_cashback_from_month(self, month: int, year: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_used_cashback_from_month(self, month: int, year: int) -> int:
        raise NotImplementedError
