from models import User
from db import db
import peewee

class UserRepository:
    def create(self, user: User) -> None:
        try:
            db.create_tables([User])
            print("Tabela 'User' criada com sucesso!")
        except peewee.OperationalError:
            print("Tabela 'User' ja existe!")
        User.create(name=user.name, password=user.password)

    def list_all(self) -> list:
        query = User.select().execute()
        return query

    def update(self, old_name: str ,user:User) -> None:
        User.update(name=user.name, password=user.password).where(User.name == old_name).execute()

    def delete(self, id):
        User.delete().where(User.id == id).execute()