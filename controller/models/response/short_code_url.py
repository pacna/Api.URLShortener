from pydantic.fields import Field
from controller.models.base_config_model import BaseConfigModel


class ShortCodeURLResponse(BaseConfigModel):
    url: str = Field(None, alias='url')
