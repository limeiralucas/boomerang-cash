from datetime import datetime
from beanie import Insert, Replace, SaveChanges, Update, before_event
from pydantic import BaseModel


class AutoTimestampMixin(BaseModel):
    @before_event(Insert)
    def set_created_at(self):
        if getattr(self, "created_at") is not None:
            self.created_at = datetime.now()

    @before_event(Update, SaveChanges, Replace)
    def set_updated_at(self):
        if getattr(self, "updated_at") is not None:
            self.updated_at = datetime.now()
