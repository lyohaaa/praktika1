from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    date_of_birth = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, unique = True, index=True)
    citizenship = Column(String, index=True)

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    user_id = (Integer, ForeignKey("users.id"))

    user = relationship("User")

class Cars(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer, index=True)
    color = Column(String, index=True)
    drive_type = Column(String, index=True)
    engine_type = Column(String, index=True)
    body_type = Column(String, index=True)
    volume = Column(Integer, index=True)
    petrol_type = Column(Integer, index=True)

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    product_id = Column(Integer, ForeignKey("products.id"), index=True)
    car_id = Column(Integer, ForeignKey("cars.id"), index=True)
    total_amount = Column(Integer, index=True)
    place = Column(Integer, index=True)

    user = relationship("User", "Products", "Cars")

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer, index=True)
    stock = Column(Integer, index=True)