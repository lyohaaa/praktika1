from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.models import Car

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)
Base = declarative_base()

def create_test_data():
    db = SessionLocal()

    db.query(Car).delete()

    test_cars = [
        Car(            
            id = 1,
            brand = "Porsche", model = "Taycan", year = "2023", color = "Black",
            body_type = "Sedan", fuel_type = "Hybrid", drive_type = "Front-wheel",
            transmission_type = "Automatic", interior_type = "Leather",
            engine_type = "2.5L 4-Cylinder", price = "32000",
            image_url = "https://clck.ru/3MKARd", is_available = True
            ),
        Car(
            id = 2,
            brand = "Toyota", model = "Camry", year = "2024", color = "White",
            body_type = "Coupe", fuel_type = "Petrol", drive_type = "Rear-wheel",
            transmission_type = "Manual", interior_type = "Eco-Leather",
            engine_type = "5.0L V8", price = "45000",
            image_url = "https://clck.ru/3MKBGz", is_available = False
        ),
        Car(
            id = 3,
            brand = "Ford", model = "Mustang", year = "2022", color = "Gray",
            body_type = "Sedan", fuel_type = "Petrol", drive_type = "Rear-wheel",
            transmission_type = "Manual", interior_type = "Cloth",
            engine_type = "4.5L V4", price = "55000",
            image_url = "https://clck.ru/3MKBTM", is_available = True
        ),
        Car(
            id = 4,
            brand = "Tesla", model = "Model Y", year = "2023", color = "White",
            body_type = "Sedan", fuel_type = "Electric", drive_type = "All-wheel",
            transmission_type = "Automatic", interior_type = "Vegan-leather",
            engine_type = "Dual Motor", price = "95000",
            image_url = "https://clck.ru/3MKBiD", is_available = True
        ),
        Car(
            id = 5,
            brand = "Honda", model = "Civic", year = "2024", color = "Blue",
            body_type = "CVT", fuel_type = "Petrol", drive_type = "All-wheel",
            transmission_type = "Automatic", interior_type = "Fabric",
            engine_type = "1.5L Turbo", price = "25000",
            image_url = "https://clck.ru/3MKBsB", is_available = True
        ),
        Car(
            id = 6,
            brand = "BMW", model = "X5", year = "2022", color = "Red",
            body_type = "SUV", fuel_type = "Petrol", drive_type = "Rear-wheel",
            transmission_type = "Automatic", interior_type = "Leather",
            engine_type = "2.0L Turbo", price = "55000",
            image_url = "https://clck.ru/3MKByd", is_available = True
        ),
        Car(
            id = 7,
            brand = "Mercedes", model = "C-Class", year = "2023", color = "Black",
            body_type = "Sedan", fuel_type = "Petrol", drive_type = "Rear-wheel",
            transmission_type = "Automatic", interior_type = "Leather",
            engine_type = "2.0L Turbo", price = "65000",
            image_url = "https://clck.ru/3MKCA2", is_available = True
        ),
        Car(
            id = 8,
            brand = "Audi", model = "A4", year = "2020", color = "Purple",
            body_type = "Sedan", fuel_type = "Petrol", drive_type = "All-wheel",
            transmission_type = "Automatic", interior_type = "Leather",
            engine_type = "2.0L Turbo", price = "75000",
            image_url = "https://clck.ru/3MKCFz", is_available = True
        ),
        Car(
            id = 9,
            brand = "Volkswagen", model = "Golf", year = "2021", color = "White",
            body_type = "Hatchback", fuel_type = "Petrol", drive_type = "Front-wheel",
            transmission_type = "Manual", interior_type = "Fabric",
            engine_type = "1.5L Turbo", price = "30000",
            image_url = "https://clck.ru/3MKCRD", is_available = True
        ),
        Car(
            id = 10,
            brand = "Kia", model = "Sportage", year = "2023", color = "Green",
            body_type = "SUV", fuel_type = "Hybrid", drive_type = "All-wheel",
            transmission_type = "Automatic", interior_type = "Leather",
            engine_type = "1.6L Turbo", price = "35000",
            image_url = "https://clck.ru/3MKCc2", is_available = True
        )
    ]

    db.add_all(test_cars)
    db.commit()

    print("Тестовые данные успешно созданы")