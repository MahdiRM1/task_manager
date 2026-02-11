from sqlalchemy.orm import Session

from app.adapters.Exceptions import IdNotFound
from app.adapters.models.UserModel import UserModel
from app.core.entities.User import User
from app.domain.repositories.UserRepository import UserRepository


class SqlUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, user: User) -> None:
        model = UserModel(name = user.name)
        self.session.add(model)
        self.session.flush()
        user._set_id(model.id)

    def remove(self, user: User) -> None:
        model = self.session.get(UserModel, user.get_id())
        if model:
            self.session.delete(model)

    def update(self, user: User) -> None:
        user_model = self.session.get(UserModel, user.get_id())
        if user_model:
            user_model.name = user.name

    def get_by_id(self, user_id: int) -> User:
        model = self.session.get(UserModel, user_id)

        if not model:
            raise IdNotFound(f"User id {user_id} not found")

        user = User(model.name)
        user.id = model.id
        return user

    def has_tasks(self, user_id: int) -> bool:
        model = self.session.get(UserModel, user_id)
        return bool(model and model.tasks)