from pydantic.fields import Field
from controllers.models.base_config_model import BaseConfigModel


class GotoResponse(BaseConfigModel):
    url: str = Field(None, alias='url')
