import pytest
from src.database import Base, engine, SessionLocal

@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.rollback() 
    Base.metadata.drop_all(bind=engine) 