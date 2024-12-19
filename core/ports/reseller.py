from abc import ABC, abstractmethod

from core.models.reseller import Reseller


class ResellerRepository(ABC):
    """Abstract base class that defines the interface for reseller operations."""

    @abstractmethod
    async def create_reseller(self, reseller: Reseller) -> Reseller:
        """Creates a new reseller.

        Args:
            reseller (Reseller): The reseller to be created.

        Returns:
            Reseller: The created reseller.
        """
        pass

    @abstractmethod
    async def get_reseller_by_email(self, email: str) -> Reseller:
        """Retrieves a reseller by their email address.

        Args:
            email (str): The email address of the reseller to be retrieved.

        Returns:
            Reseller: The reseller with the specified email address.
        """
        pass


class ResellerService(ABC):
    @abstractmethod
    async def create_reseller(self, reseller: Reseller) -> Reseller:
        raise NotImplementedError

    @abstractmethod
    async def get_reseller_by_email(self, email: str) -> Reseller:
        raise NotImplementedError
