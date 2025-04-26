from src.database import Base
from sqlalchemy import Column, String

class User(Base):
    __tablename__ = "users"
    email = Column(String, primary_key=True, unique=True)
    password = Column(String, nullable=False)