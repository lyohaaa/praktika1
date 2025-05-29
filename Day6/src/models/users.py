from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.database import Base
import enum

class UserRole (enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User (Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    role = Column(String, default="user")
    full_name = Column(String, nullable = False)
    birth_date = Column(DateTime, nullable = True)
    driving_experience = Column(Integer, nullable = True)
    citizenship = Column(String, nullable = True)
    inn = Column(String, nullable = True)
    email = Column(String, unique = True, index = True, nullable = False)
    password_hash = Column(String, nullable = False)
    created_at = Column(DateTime, server_default=func.now())

    # orders = relationship("Order", back_populates="user")
