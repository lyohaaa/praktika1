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