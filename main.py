import psycopg2
from database.db import Database

from entity.user import User
from repository.user import UserRepository

if __name__ == '__main__':
    db = Database()
    db.connect()

    userRepo = UserRepository()

    option = -1
    while option != 0:
        print("1 - Criar Usuário")
        print("2 - Listar usuários")
        print("0 - Sair")

        option = int(input())

        if option == 1:
            newUser = User.new()
            print("Informe os dados do usuário:\n")
            print("Nome:")
            newUser.name = input()
            print("Email:")
            newUser.email = input()
            print("Senha:")
            newUser.password = input()

            userRepo.insert(newUser)
        elif option == 2:
            print("Usuários: ")
            users = userRepo.list()
            for user in users:
                print(user)

    print("Saindo...")
