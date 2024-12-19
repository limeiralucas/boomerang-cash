from core.models.reseller import Reseller
from core.ports.reseller import ResellerRepository as IResellerRepository


class ResellerRepository(IResellerRepository):
    async def create_reseller(self, reseller: Reseller) -> Reseller:
        pass

    async def get_reseller_by_email(self, email: str) -> Reseller:
        pass
