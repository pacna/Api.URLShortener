from pydantic.main import BaseModel


class BaseConfigModel(BaseModel):
    class Config:
        allow_population_by_field_name = True
