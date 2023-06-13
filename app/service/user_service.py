from app.model.user import User

class UserService:
        
    def create(self, username, password, email) -> tuple:
        user_info = User(username=username, password=password, email=email)
        return user_info.save()
    