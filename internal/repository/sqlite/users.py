from sqlalchemy.orm import Session

from internal.repository.models.errors import NotFoundError
from internal.repository.models.users import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def Create(self, username: str, hashed_password: str):
        try:
            new_user = User(
                username=username,
                hashed_password=hashed_password
            )

            self.db.add(new_user)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadByUsername(self, username: str) -> User:
        try:
            user = self.db.query(User).filter(User.username == username).first()
            if user:
                return user
            else:
                raise NotFoundError()
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadByID(self, id: int) -> User:
        try:
            user = self.db.query(User).filter(User.id == id).first()
            if user:
                return user
            else:
                raise NotFoundError()
        except Exception as e:
            self.db.rollback()
            raise e

    def Delete(self, id: int):
        try:
            user = self.ReadByID(id)
            self.db.delete(user)  # Mark the user for deletion
            self.db.commit()  # Commit to apply the deletion
        except Exception as e:
            self.db.rollback()
            raise e

    def Update(self, id: int, username: str, hashed_password: str):
        try:
            user = self.ReadByID(id)
            user.username = username
            user.hashed_password = hashed_password  # Update the password field
            self.db.commit()  # Commit the change to the database
        except Exception as e:
            self.db.rollback()
            raise e

    def ReadAll(self):
        try:
            return self.db.query(User).all()
        except Exception as e:
            self.db.rollback()
            raise e
