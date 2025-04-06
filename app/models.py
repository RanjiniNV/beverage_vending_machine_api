from app.utils.common_imports import *


class inventory_items(BaseModel):
    milk: int
    sugar: int
    water: int
    coffee: int


class new_recipe(BaseModel):
    name: str
    milk: int
    sugar: int
    water: int
    coffee: int
