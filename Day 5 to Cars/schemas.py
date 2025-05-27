from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional

### Вместо review - cars

class UserCreate (BaseModel):
    full_name: str
    email: EmailStr

class UserOut (BaseModel):
    id: int
    full_name: str
    email: EmailStr

    class Config:
        orm_mode = True

class CategoryCreate (BaseModel):
    name: str

class CategoryOut (BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class ReviewCreate (BaseModel):
    reviewer_name: str
    comment: Optional[str] = None
    rating: float = Field(..., ge = 0, le = 5)

class ReviewOut (BaseModel):
    id: int
    reviewer_name: str
    comment: Optional[str]
    rating: float
    created_at: datetime

    class Config:
        orm_mode = True

class ProductCreate (BaseModel):
    title: str
    content: str
    category_id: int
    author_ids: List[int]

class ProductOut (BaseModel):
    id: int
    title: int
    content: str
    published_at: datetime
    category: CategoryOut
    authors: List[UserOut]
    reviews: List[ReviewOut] = []

class ProductUpdate (BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category_id: Optional[int] = None
    author_ids: Optional[List[int]] = None