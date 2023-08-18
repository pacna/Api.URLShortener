from typing import List
from pydantic.fields import Field
from controllers.models.base_config_model import BaseConfigModel


class ShortCodeResponse(BaseConfigModel):
    url: str | None = Field(None, alias='url')
    id: str | None = Field(None, alias='id')


class ShortCodeCollectionResponse(BaseConfigModel):
    list: List[ShortCodeResponse] = Field(None, alias='list')
    count: int = Field(None, alias='count')
