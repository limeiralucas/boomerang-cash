from typing import Annotated, Any
from pydantic import AfterValidator, Field
from pydantic.json_schema import SkipJsonSchema

ExcludedField = SkipJsonSchema[
    Annotated[Any, Field(default=None, exclude=True), AfterValidator(lambda _: None)]
]
