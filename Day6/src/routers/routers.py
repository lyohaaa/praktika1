from typing import List, Optional
from fastapi import APIRouter, Depends,  HTTPException, Query
from sqlalchemy.orm import Session
from src.models import Car
from src.schemas import CarResponse, FilterOptions
from src.database import get_db

router = APIRouter(prefix="/cars", tags=["cars"])

@router.get("/", response_model = List[CarResponse])
def get_cars (
    brand: Optional[str] = None,
    color: Optional[str] = None,
    min_price: Optional[str] = None,
    max_price: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Car)

    if brand:
        query = query.filter(Car.brand == brand)
    if color:
        query = query.filter(Car.color == color)
    if min_price:
        query = query.filter(Car.price >= min_price)
    if max_price:
        query = query.filter(Car.price <= max_price)

    return query.all()

@router.get("/filter-options", response_model=FilterOptions)
def get_filter_options(db: Session = Depends(get_db)):
    return {
        "body_types": db.query(Car.body_type).distinct.all(),
        "fuel_types": db.query(Car.fuel_type).distinct.all(),
        "drive_types": db.query(Car.drive_type).distinct.all(),
        "transmission_types": db.query(Car.transmission_type).distinct.all(),
        "interior_types": db.query(Car.interior_type).distinct.all(),
        "engine_types": db.query(Car.body_type).distinct.all()
    }