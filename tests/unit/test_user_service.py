from src.services.user_service import UserService
from src.models.user import User

def test_create_user(db):
    user = UserService.create_user("test@example.com", "pass123")
    assert user.email == "test@example.com"
    assert db.query(User).filter(User.email == "test@example.com").first()