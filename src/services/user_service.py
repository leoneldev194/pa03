from src.database import get_db
from src.models.user import User

class UserService:
    @staticmethod
    def create_user(email: str, password: str):
        db = next(get_db())
        user = User(email=email, password=password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user