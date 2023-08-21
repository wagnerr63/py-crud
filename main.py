import psycopg2
from database.db import Database

from entity.user import User
from repository.user import UserRepository

if __name__ == '__main__':
    db = Database()
    db.connect()

    userRepo = UserRepository()

    print('hello')
    newUser = User.new()
    print("Informe os dados do usuário:\n")
    print("Nome:")
    newUser.name = input()
    print("Email:")
    newUser.email = input()
    print("Senha:")
    newUser.password = input()

    userRepo.insert(newUser)
