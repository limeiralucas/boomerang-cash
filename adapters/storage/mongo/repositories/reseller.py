from beanie import Document
from passlib.context import CryptContext

from core.models.reseller import Reseller
from core.ports.reseller import ResellerRepository as IResellerRepository


class ResellerDocument(Document, Reseller):
    class Settings:
        name = "resellers"

    @staticmethod
    def from_entity(entity: Reseller):
        return ResellerDocument.model_validate(entity.model_dump())


class ResellerRepository(IResellerRepository):
    @staticmethod
    def hash_password(password: str) -> str:
        return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)

    async def create_reseller(self, reseller: Reseller) -> Reseller:
        reseller_obj = ResellerDocument.from_entity(reseller)
        reseller_obj.password = ResellerRepository.hash_password(reseller_obj.password)

        return await ResellerDocument.insert_one(reseller_obj)

    async def get_reseller_by_email(self, email: str) -> Reseller:
        return await ResellerDocument.find_one({"email": email})
