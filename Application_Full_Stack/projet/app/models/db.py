from .database import SessionLocal, engine, BaseSQL
from sqlalchemy import Column, Integer, String

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Define the User model
class User(BaseSQL):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    boards_generated = Column(Integer, index=True, default=None, nullable=True)
    profile_picture = Column(String, nullable=True)