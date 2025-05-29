from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import Optional, List
from datetime import date, datetime

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

class CarResponse (CarBase):
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

class UserCreate(BaseModel):
    role: Optional[str] = "user"
    full_name: str
    birth_date: date
    driving_experience: Optional[int] = None
    citizenship: Optional[str] = None
    inn: Optional[str] = None
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    role: Optional[str] = None
    full_name: Optional[str] = None
    birth_date: Optional[date] = None
    driving_experience: Optional[int] = None
    citizenship: Optional[str] = None
    inn: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    role: str
    full_name: str
    birth_date: date
    driving_experience: Optional[int]
    citizenship: Optional[str]
    inn: Optional[str]
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class ReferenceTypeResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class ReferenceTypeCreate(BaseModel):
    name: str

class ReferenceTypeUpdate(BaseModel):
    name: Optional[str] = None

class BodyTypeResponse(ReferenceTypeResponse):
    pass

class FuelTypeResponse(ReferenceTypeResponse):
    pass

class DriveTypeResponse(ReferenceTypeResponse):
    pass

class TransmissionTypeResponse(ReferenceTypeResponse):
    pass 

class InteriorTypeResponse(ReferenceTypeResponse):
    pass 

class EngineTypeResponse(ReferenceTypeResponse):
    pass 

class CarBase(BaseModel):
    name: str 
    year: int
    engine_id: int
    drive_id: int
    transmission_id: int
    interior_id: int
    fuel_tank_capacity: float
    fuel_type_id: int
    cruise_control: bool
    body_type_id: int
    max_speed: int
    fuel_consumption: float
    price: float

class CarCreate(CarBase):
    pass 

class CarUpdate(BaseModel):
    name: Optional[str] = None
    year: Optional[int] = None
    engine_id: Optional[str] = None
    drive_id: Optional[int] = None
    transmission_id: Optional[str] = None
    interior_id: Optional[str] = None
    fuel_tank_capacity: Optional[float] = None
    fuel_type_id: Optional[int] = None
    cruise_control: Optional[bool] = None
    body_type_id: Optional[int] = None
    max_speed: Optional[int] = None
    fuel_consumption: Optional[float] = None
    price: Optional[float] = None
    url_image: Optional[str] = None

class CarResponse(CarBase):
    id: int
    url_image: Optional[str] = None
    engine: EngineTypeResponse
    drive: DriveTypeResponse
    transmission: TransmissionTypeResponse
    interior: InteriorTypeResponse
    fuel_type: FuelTypeResponse
    body_type: BodyTypeResponse

    class Config:
        from_attributes = True