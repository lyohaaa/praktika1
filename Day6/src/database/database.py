from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.models import Car

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)
Base = declarative_base()

def create_test_data():
    db = SessionLocal()

    db.query(Car).delete()

    test_cars = [
        Car(
            ... ### Машины дописать
        )
    ]

    db.add_all(test_cars)
    db.commit()
    db.close