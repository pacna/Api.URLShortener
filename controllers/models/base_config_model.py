from pydantic.main import BaseModel


class BaseConfigModel(BaseModel):
    class Config:
        populate_by_name = True
