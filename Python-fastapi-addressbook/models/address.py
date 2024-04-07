from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import registry
from models.base import BASE

mapper_registry = registry()


class Address(BASE):
    __tablename__ = "addresses"
    __table_args__ = (UniqueConstraint("id"),)

    def __init__(self, data_dict):
        data_dict = dict(data_dict)
        for key in data_dict:
            lower_key = key.lower()
            setattr(self, lower_key, data_dict[key])

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
