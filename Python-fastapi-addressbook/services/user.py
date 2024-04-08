from services.base import BaseDataManager, BaseService
from models.user import User
from sqlalchemy import select, and_


class UserService(BaseService):
    def convert_data_into_obj(self, input_data: dict):
        res = UserDataManager(self.session).insertData(User(input_data))
        return res


class UserDataManager(BaseDataManager):

    def insertData(self, data: User) -> User:
        return self.add_one(data)

    def get_user(self, data) -> User:
        # self.session.query(User).filter()
        stmt = select(User).where(
            and_(User.email == data.email, User.password == data.password)
        )
        return self.get_one(stmt)
