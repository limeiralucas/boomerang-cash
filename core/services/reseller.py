from core.models.reseller import Reseller
from core.ports.reseller import ResellerRepository
from core.ports.reseller import ResellerService as IResellerService


class ResellerService(IResellerService):
    def __init__(self, reseller_repository: ResellerRepository):
        self.reseller_repository = reseller_repository

    async def create_reseller(self, reseller) -> Reseller:
        return await self.reseller_repository.create_reseller(reseller)

    async def get_reseller_by_email(self, email) -> Reseller:
        return await self.reseller_repository.get_reseller_by_email(email)
