from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import Base
from database import engine

app = FastAPI(
    title="API_PRAKTIKA",
    description="API",
    version="1.0.0"
)

tasks = []
users = []
cars = []
rent = []


Base.metadata.create_all(engine)

@app.get("/rent")
def get_rent():
    return rent

@app.post("/rent")
def add_rent(task: str):
    rent.append(rent)
    return {"message": "Аренда обновлена"}

@app.put("/rent")
def update_rent(old: str, new: str):
    if old in rent:
        index = rent.index(old)
        rent[index] = new
        return {"message": "Обновлено", "item": new}
    
@app.delete("/rent")
def delete_rent(item, str):
    if item in rent:
        rent.remove(item)
        return {"message": "Машина удалена", "item": item}

#####################################################

@app.get("/cars")
def get_cars():
    return cars

@app.post("/cars")
def add_car(task: str):
    cars.append(cars)
    return {"message": "Машина обновлена"}

@app.put("/cars")
def update_car(old: str, new: str):
    if old in cars:
        index = cars.index(old)
        cars[index] = new
        return {"message": "Обновлено", "item": new}
    
@app.delete("/cars")
def delete_car(item, str):
    if item in cars:
        cars.remove(item)
        return {"message": "Машина удалена", "item": item}

#####################################################

@app.get("/users")
def get_users():
    return users

@app.post("/users")
def add_user(task: str):
    users.append(users)
    return {"message": "Пользователь обновлён"}

@app.put("/")
def update_user(old: str, new: str):
    if old in users:
        index = users.index(old)
        users[index] = new
        return {"message": "Обновлено", "item": new}
    
@app.delete("/")
def delete_user(item, str):
    if item in users:
        users.remove(item)
        return {"message": "Пользователь удалён", "item": item}


#################################


@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Задача обновлена"}

@app.put("/")
def update_item(old: str, new: str):
    if old in tasks:
        index = tasks.index(old)
        tasks[index] = new
        return {"message": "Обновлено", "item": new}
    
@app.delete("/")
def delete_item(item, str):
    if item in tasks:
        tasks.remove(item)
        return {"message": "Удалено", "item": item}
    
@app.get("/contacts")
def get_contacts():
    return {
        "tel": "8 800 555 35 34",
        "email": "aaa@aaa.aaa"
    }