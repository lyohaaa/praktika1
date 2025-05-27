from fastapi import APIRouter

router = APIRouter()

@router.get("/{id}", response_model = CarResponse)
def get_car (id: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == id).first()
    if not car:
        raise HTTPException(status_code = 404, detail = "Не найдено")
    return car

app.include_router (car.router, prefix = "/cars", tags = ["cars"])