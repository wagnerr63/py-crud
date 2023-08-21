import uuid
from datetime import datetime


class User:
    id: str = ""
    name: str = ""
    email: str = ""
    password: str = ""
    created_at: datetime = ""
    updated_at: datetime = ""

    @staticmethod
    def new():
        user = User
        user.id = uuid.uuid4().__str__()
        user.created_at = datetime.now()
        user.updated_at = datetime.now()

        return user
