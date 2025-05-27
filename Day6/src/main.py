from fastapi import FastAPI
from src.routers import car, reference, auth
from src.database import create_test_data

app = FastAPI()

app.include_router(auth.router)
app.include_router(car.router)
app.include_router(reference.router)

@app.on_event("startup")
def on_startup():
    create_test_data()