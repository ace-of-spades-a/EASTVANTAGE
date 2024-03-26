from services.base import BaseDataManager, BaseService
from models.books import Book
from sqlalchemy import select


class BookService(BaseService):
    def convert_data_into_obj(self, input_data: dict):
        res = BookDataManager(self.session).insertData(Book(input_data))
        return res


class BookDataManager(BaseDataManager):

    def insertData(self, data: Book):
        return self.add_one(data)

    def get_book(self, book_id):
        stmt = select(Book).where(Book.id == book_id)
        return self.get_one(stmt)
