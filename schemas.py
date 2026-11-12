from pydantic import BaseModel

class PlantBase(BaseModel):
    is_active: bool
    plant_name: str
    water_freq: int
    outdoor: bool

class PlantCreate(PlantBase):
    pass

class PlantUpdate(PlantBase):
    pass

class Plant(PlantBase):
    id: int