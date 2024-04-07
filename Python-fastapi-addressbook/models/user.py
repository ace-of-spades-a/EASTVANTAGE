from sqlalchemy import Column, Integer, String
from sqlalchemy import UniqueConstraint
from models.base import BASE
from sqlalchemy.orm import registry

mapper_registry = registry()


class User(BASE):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("id"),)

    def __init__(self, data_dict):
        data_dict = dict(data_dict)
        for key in data_dict:
            lower_key = key.lower()
            setattr(self, lower_key, data_dict[key])

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)
