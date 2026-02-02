from sqlalchemy.orm import Session

from app.adapters.Models.UserModel import UserModel
from app.core.entities.User import User
from app.domain.repositories.UserRepository import UserRepository


class SqlUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, user: User) -> None:
        user_model = UserModel(name = user.name)
        self.session.add(user_model)
        self.session.flush()
        self.session.commit()
        user.id = user_model.id

    def remove(self, user: User) -> None:
        user_model = self.session.get(UserModel, user.id)
        if user_model:
            self.session.delete(user_model)
            self.session.commit()

    def update(self, user: User) -> None:
        user_model = self.session.get(UserModel, user.id)
        if user_model:
            user_model.name = user.name
            self.session.commit()

    def get_by_id(self, user_id: int) -> User | None:
        user_model = self.session.get(UserModel, user_id)

        if not user_model:
            return None

        user = User(user_model.name)
        user.id = user_model.id
        return user

    def has_tasks(self, user_id: int) -> bool:
        user_model = self.session.get(UserModel, user_id)
        return user_model and user_model.tasks