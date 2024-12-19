from datetime import datetime
from pydantic import BaseModel


class TokenData(BaseModel):
    sub: str
    exp: datetime | None
