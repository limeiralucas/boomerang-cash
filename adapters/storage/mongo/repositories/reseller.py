from beanie import Document
from core.models.reseller import Reseller
from core.ports.reseller import ResellerRepository as IResellerRepository


class ResellerDocument(Document, Reseller):
    class Settings:
        name = "resellers"

    @staticmethod
    def from_entity(entity: Reseller):
        return ResellerDocument.model_validate(entity.model_dump())


class ResellerRepository(IResellerRepository):
    async def create_reseller(self, reseller: Reseller) -> Reseller:
        return await ResellerDocument.insert_one(ResellerDocument.from_entity(reseller))

    async def get_reseller_by_email(self, email: str) -> Reseller:
        return await ResellerDocument.find_one({"email": email})
