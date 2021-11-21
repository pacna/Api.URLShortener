from typing import List
from pydantic.fields import Field
from controller.models.base_config_model import BaseConfigModel


class ShortCodeResponse(BaseConfigModel):
    url: str = Field(None, alias='url')
    short_code: str = Field(None, alias='shortCode')
    id: str = Field(None, alias='id')


class ShortCodeCollectionResponse(BaseConfigModel):
    list: List[ShortCodeResponse] = Field(None, alias='list')
    count: int = Field(None, alias='count')
