from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base

DATABASE_URL = "sqltie:///./app.db"
engine = create_engine(
    DATABASE_URL,
    connect_args = {"check_same_thread": False} # Для SQLite
)

Base.metadata.create.all(bind = engine)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

