from datetime import datetime
from pydantic import BaseModel, Field


class TimestampMixin(BaseModel):
    """
    Mixin class to add timestamp fields to a model.

    Attributes:
        created_at (datetime): The datetime when the record was created.
            Defaults to the current datetime.
        updated_at (datetime, optional): The datetime when the record was last updated.
            Defaults to None.
    """

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None
