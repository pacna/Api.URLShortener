from controller.models.base_config_model import BaseConfigModel
from pydantic.fields import Field


class CreateShortCodeRequest(BaseConfigModel):
    url: str = Field(None, alias='url')
