from abc import ABC, abstractmethod

from app.domain.models.reseller import Reseller


class ResellerPort(ABC):
    """
    Abstract base class that defines the interface for reseller operations.
    Methods
    -------
    create_reseller(reseller: Reseller) -> Reseller
        Creates a new reseller.
    get_reseller_by_email(email: str) -> Reseller
        Retrieves a reseller by their email address.
    """

    @abstractmethod
    def create_reseller(self, reseller: Reseller) -> Reseller:
        pass

    @abstractmethod
    def get_reseller_by_email(self, email: str) -> Reseller:
        pass
