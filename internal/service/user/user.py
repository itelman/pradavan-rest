import bcrypt
from sqlalchemy.orm import Session

from internal.repository.models.errors import NotFoundError, UnauthorizedError
from internal.repository.models.users import User
from internal.repository.sqlite.users import UserRepository
from internal.validation.users import UserRequest


class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def Authenticate(self, req: UserRequest) -> User:
        username, password = req.username, req.password

        try:
            user = self.user_repository.ReadByUsername(username)

            if not bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
                raise UnauthorizedError()

            return user
        except NotFoundError:
            raise UnauthorizedError()
        except Exception as e:
            raise e

    def Register(self, req: UserRequest) -> int:
        username, password = req.username, req.password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        self.user_repository.Create(username.lower(), hashed_password)

    def Get(self, id: int) -> User:
        return self.user_repository.ReadByID(id)

    def Delete(self, user_id):
        self.user_repository.Delete(user_id)

    def Update(self, user_id: int, req: UserRequest) -> int:
        username, password = req.username, req.password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        self.user_repository.Update(user_id, username.lower(), hashed_password)

    def GetAll(self):
        return self.user_repository.ReadAll()
