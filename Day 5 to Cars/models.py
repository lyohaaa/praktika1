from sqlalchemy import Boolean, Column, Integer, String, Text, ForeignKey, DateTime, Table, Float
from sqlalchemy.orm import relationship, declarative_base
from database import datetime

Base = declarative_base()

# Связующая таблица для статьи и авторов
product_users = Table(
    "product_users",
    Base.metadata,
    Column ("product_id", ForeignKey ("product.id"), primary_key = True),
    Column ("user_id", ForeignKey ("user.id"), primary_key = True)
)

class User (Base):
    __tablename__ = "users"

    id = Column (Integer, primary_key = True)
    full_name = Column (String, nullable = False)
    email = Column (String, unique = True, nullable = False)

    products = relationship ("Product", secondary = product_users, back_populates = "users")

class Category (Base):
    __tablename__ = "categories"

    id = Column (Integer, primary_key = True)
    name = Column (String, unique = True, nullable = False)

class Product (Base):
    __tablename__ = "products"

    id = Column (Integer, primary_key = True)
    title = Column (String, nullable = False)
    content = Column (Text, nullable = False)
    published_at = Column (DateTime, default = datetime.utcnow)
    category_id = Column (Integer, ForeignKey("categories.id"))

    category = relationship ("Category")
    users = relationship ("User", secondary = product_users, back_populates = "products")
    reviews = relationship ("Review", back_populates = "product")

class Review (Base):
    __tablename__ = "reviews"

    id = Column (Integer, primary_key = True)
    reviewer_name = Column (String, nullable = False)
    comment = Column (Text)
    rating = Column (Float, nullable = False)
    created_at = Column (DateTime, default = datetime.utcnow)

    product_id = Column (Integer, ForeignKey("products.id"))
    product = relationship ("Product", back_populates = "reviews")






##################################### 6 день
class BodyType (Base):
    __tablename__ = "body_types"
    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True, nullable = False)

class FuelType (Base):
    __tablename__ = "fuel_types"
    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True, nullable = False)

class DriveType (Base):
    __tablename__ = "drive_types"
    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True, nullable = False)

class TransmissionType (Base):
    __tablename__ = "transmission_types"
    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True, nullable = False)

class InteriorType (Base):
    __tablename__ = "interior_types"
    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True, nullable = False)

class EngineType (Base):
    __tablename__ = "engine_types"
    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True, nullable = False)

class Car (Base):
    __tablename__ = "cars"
    id = Column (Integer, primary_key = True, index = True)
    name = Column (String, nullable = False)
    year = Column (Integer, nullable = False)
    engine_id = Column (Integer, ForeignKey("engine_types.id"), nullable = False)
    drive_id = Column (Integer, ForeignKey("drive_types.id"), nullable = False)
    transmission_id = Column (Integer, ForeignKey("transmission_types.id"), nullable = False)
    interior_id = Column (Integer, ForeignKey("interior_types.id"), nullable = False)
    fuel_tank_capacity = Column (Float, nullable = False)
    fuel_type_id = Column (Integer, ForeignKey("fuel_types.id"), nullable = False)
    cruise_control = Column (Boolean, default = False)
    body_type_id = Column (Integer, ForeignKey("body_types.id"), nullable = False)
    max_speed = Column (Integer, nullable = False)
    fuel_consumption = Column (Float, nullable = False)
    price = Column (Float, nullable = False)
    url_image = Column (String, nullable = True)