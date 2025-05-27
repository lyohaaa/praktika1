from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import Optional, List

class CarBase (BaseModel):
    brand: str = Field(..., min_length=1, max_length=50)
    model:str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., gt = 1900, lt = 2100)
    color: str = Field(..., min_length=3, max_length=50)
    body_type: str = Field(..., min_length=3, max_length=50)
    fuel_type: str = Field(..., min_length=3, max_length=50)
    drive_type:str = Field(..., min_length=3, max_length=50)
    transmission_type:str = Field(..., min_length=3, max_length=50)
    interior_type:str = Field(..., min_length=3, max_length=50)
    engine_type:str = Field(..., min_length=3, max_length=50)
    price: int = Field(..., gt = 0)
    image_url: HttpUrl
    is_available: bool = True

class CarCreate (CarBase):
    pass

class CarRespone (CarBase):
    id: int

    class Config:
        orm_mode = True

class FilterOptions (BaseModel):
    body_types: List[str]
    fuel_types: List[str]
    drive_types: List[str]
    transmission_types: List[str]
    interior_types: List[str]
    engine_types: List[str]