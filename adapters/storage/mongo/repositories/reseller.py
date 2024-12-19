from typing import Annotated
from beanie import Document, Indexed
from pymongo.errors import DuplicateKeyError
from passlib.context import CryptContext
from pydantic import EmailStr
from pydantic_br import CPFDigits

from core.models.reseller import Reseller
from core.ports.reseller import (
    ResellerAlreadyExists,
    ResellerRepository as IResellerRepository,
)


class ResellerDocument(Document, Reseller):
    email: Annotated[EmailStr, Indexed(unique=True)]
    cpf: Annotated[CPFDigits, Indexed(unique=True)]

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

        try:
            return await ResellerDocument.insert_one(reseller_obj)
        except DuplicateKeyError as ex:
            raise ResellerAlreadyExists() from ex

    async def get_reseller_by_email(self, email: str) -> Reseller:
        return await ResellerDocument.find_one({"email": email})
