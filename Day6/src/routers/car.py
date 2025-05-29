import os
import shutil
from typing import List, Optional
from uuid import uuid4
from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile
from sqlalchemy.orm import Session
from src.auth import require_role
from src.models.users import UserRole, User
from src.models.car import BodyType, Car, DriveType, EngineType, FuelType, InteriorType, TransmissionType
from src.schemas.scheme import CarCreate, CarResponse, FilterOptions
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

@router.get("/", response_model=List[CarResponse])
def get_cars(
    db: Session = Depends(get_db),
    body_type_id: List[int] | None = Query(default= None),
    fuel_type_id: List[int] | None = Query(default= None),
    drive_id: List[int] | None = Query(default= None),
    transmission_id: List[int] | None = Query(default= None),
    interior_id: List[int] | None = Query(default= None),
    engine_id: List[int] | None = Query(default= None),
    cruise_control: List[bool] | None = Query(default= None),
):
    query = db.query(Car)
    if body_type_id:
        query = query.filter(Car.body_type_id.in_(body_type_id))
    if fuel_type_id:
        query = query.filter(Car.fuel_type_id.in_(fuel_type_id))
    if drive_id:
        query = query.filter(Car.drive_id.in_(drive_id))
    if transmission_id:
        query = query.filter(Car.transmission_id.in_(transmission_id))
    if interior_id:
        query = query.filter(Car.interior_id.in_(interior_id))
    if engine_id:
        query = query.filter(Car.engine_id.in_(engine_id))
    if cruise_control is not None:
        query = query.filter(Car.cruise_control.in_(cruise_control))
    return query.all()

@router.post("/", response_model = CarResponse, status_code = 201)
def create_car(
    car: CarCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN))
):
    if not db.query(EngineType).filter(EngineType.id == car.engine_id).first():
        raise HTTPException(status_code=400, detail = "Неправильный engine_id")
    if not db.query(EngineType).filter(EngineType.id == car.drive_id).first():
        raise HTTPException(status_code=400, detail = "Неправильный drive_id")
    if not db.query(EngineType).filter(EngineType.id == car.transmission_id).first():
        raise HTTPException(status_code=400, detail = "Неправильный transmission_id")
    if not db.query(EngineType).filter(EngineType.id == car.interior_id).first():
        raise HTTPException(status_code=400, detail = "Неправильный interior_id")
    if not db.query(EngineType).filter(EngineType.id == car.fuel_type_id).first():
        raise HTTPException(status_code=400, detail = "Неправильный fuel_type_id")
    if not db.query(EngineType).filter(EngineType.id == car.body_type_id).first():
        raise HTTPException(status_code=400, detail = "Неправильный body_type_id")
    
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

IMAGE_DIR = "static/images"
os.makedirs(IMAGE_DIR, exist_ok = True)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif"}
MAX_FILE_SIZE = 5 * 1024 * 1024

@router.post("/{id}/image", response_model = CarResponse)
async def upload_car_image(
    id: int,
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN))
):
    db_car = db.query(Car).filter(Car.id == id).first()
    if not db_car:
        raise HTTPException(status_code = 404, detail="Машина не найдена")
    
    file_ext = os.path.splitext(image.filename)[1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Неправильное расширение файла")
    
    image.file.seek(0, os.SEEK_END)
    file_size = image.file.tell()
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Файл слишком большой")
    image.file.seek(0)

    if db_car.url_image:
        old_file_path = db_car.url_image.replace("/static", "/static")
        if os.path.exists(old_file_path):
            os.remove(old_file_path)

    file_name = f"car_{db_car.id}_{uuid4()}{file_ext}"
    file_path = os.path.join(IMAGE_DIR, file_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    db_car.url_image = f"/static/static/{file_name}"
    db.commit()
    db.refresh(db_car)
    return db_car

@router.get("/filter-options")
def get_filter_options(db: Session = Depends(get_db)):
    return {
        "body_types": db.query(BodyType).all(),
        "fuel_types": db.query(FuelType).all(),
        "drive_types": db.query(DriveType).all(),
        "transmission_types": db.query(TransmissionType).all(),
        "interior_types": db.query(InteriorType).all(),
        "engine_types": db.query(EngineType).all(),
    }