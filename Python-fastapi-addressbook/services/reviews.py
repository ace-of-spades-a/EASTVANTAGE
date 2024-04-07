from services.base import BaseDataManager, BaseService
from models.reviews import Reviews
from sqlalchemy import select


class ReviewService(BaseService):
    def convert_data_into_obj(self, input_data: dict) -> dict:
        id = ReviewDataManager(self.session).insertData(Reviews(input_data))
        return {"id": id}


class ReviewDataManager(BaseDataManager):

    def insertData(self, data: Reviews) -> int:
        return self.add_one(data)
