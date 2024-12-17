from pydantic import BaseModel, EmailStr
from pydantic_br import CPFDigits


class Reseller(BaseModel):
    """
    Represents a reseller in the system.
    Attributes:
        first_name (str): The first name of the reseller.
        middle_name (str): The middle name of the reseller.
        last_name (str): The last name of the reseller.
        cpf (CPFDigits): The CPF (Cadastro de Pessoas Físicas) number of the reseller.
        email (EmailStr): The email address of the reseller.
        password (str): The password for the reseller's account.
    """

    first_name: str
    middle_name: str
    last_name: str
    cpf: CPFDigits
    email: EmailStr
    password: str
