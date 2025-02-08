from models import User
from db import SessionLocal
import logging
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)


class UserRepository:

    def create(self, user: User) -> int:
        logger.debug('Creating user in DB: %s', user.name)
        session = SessionLocal()
        try:
            db_user = User(name=user.name, password=user.password)
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
            return db_user.id
        except SQLAlchemyError:
            session.rollback()
            logger.exception('Error creating user %s', user.name)
            raise
        finally:
            session.close()

    def list_all(self) -> list:
        logger.debug('Listing all users')
        session = SessionLocal()
        try:
            users = session.query(User).all()
            return [{'id': u.id, 'name': u.name} for u in users]
        finally:
            session.close()

    def update(self, old_name: str, user: User) -> int:
        logger.debug('Updating user in DB: %s -> %s', old_name, user.name)
        session = SessionLocal()
        try:
            q = session.query(User).filter(User.name == old_name)
            updated = q.update({'name': user.name, 'password': user.password})
            session.commit()
            return updated
        except SQLAlchemyError:
            session.rollback()
            logger.exception('Error updating user %s', old_name)
            raise
        finally:
            session.close()

    def get_by_id(self, id):
        logger.debug('Getting user by id=%s', id)
        session = SessionLocal()
        try:
            return session.query(User).get(id)
        finally:
            session.close()

    def update_by_id(self, id, user: User) -> int:
        logger.debug('Updating user in DB by id=%s -> %s', id, user.name)
        session = SessionLocal()
        try:
            q = session.query(User).filter(User.id == id)
            updated = q.update({'name': user.name, 'password': user.password})
            session.commit()
            return updated
        except SQLAlchemyError:
            session.rollback()
            logger.exception('Error updating user id=%s', id)
            raise
        finally:
            session.close()

    def delete_by_id(self, id):
        logger.debug('Deleting user in DB id=%s', id)
        session = SessionLocal()
        try:
            deleted = session.query(User).filter(User.id == id).delete()
            session.commit()
            return deleted
        except SQLAlchemyError:
            session.rollback()
            logger.exception('Error deleting user id=%s', id)
            raise
        finally:
            session.close()

    def delete(self, id):
        return self.delete_by_id(id)
