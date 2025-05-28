from fastapi import FastAPI

import src.routers.auth_router
import src.routers.car
from .database import create_test_data

app = FastAPI()

app.include_router(src.routers.auth_router.router)
app.include_router(src.routers.car.router)

@app.on_event("startup")
def on_startup():
    create_test_data()