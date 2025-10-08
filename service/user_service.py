from models import User
from repository import UserRepository
import logging


logger = logging.getLogger(__name__)


class UserService:
    UserRepository = UserRepository()

    def create(self, user: User):
        logger.debug("Service.create called for user=%s", user.name)
        try:
            new_id = self.UserRepository.create(user)
            logger.info("User created: %s (id=%s)", user.name, new_id)
            return new_id
        except Exception as exc:
            logger.exception("Error creating user %s: %s", user.name, exc)
            raise

    def list_all(self) -> list:
        logger.debug("Service.list_all called")
        return self.UserRepository.list_all()

    def get_by_id(self, id):
        logger.debug("Service.get_by_id called id=%s", id)
        return self.UserRepository.get_by_id(id)

    def update_by_id(self, id, user: User):
        logger.debug("Service.update_by_id called id=%s", id)
        return self.UserRepository.update_by_id(id, user)

    def delete_by_id(self, id) -> int:
        logger.debug("Service.delete_by_id called id=%s", id)
        return self.UserRepository.delete_by_id(id)
