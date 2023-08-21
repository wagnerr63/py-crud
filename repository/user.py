from entity.user import User
from database.db import Database


class UserRepository:
    db: Database = None

    def __init__(self):
        db = Database()
        self.db = db
        self.db.connect()

    def insert(self, user: User):
        cursor = self.db.conn.cursor()
        cursor.execute(
            "INSERT INTO users(id, name, email, password, created_at, updated_at) VALUES(%s, %s, %s, %s, %s, %s);",
            (user.id, user.name, user.email, user.password, user.created_at, user.updated_at))
        self.db.conn.commit()

        cursor.close()
