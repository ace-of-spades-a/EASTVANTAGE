from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UniqueConstraint
from models.base import BASE
from sqlalchemy.orm import relationship, registry

mapper_registry = registry()


class Book(BASE):
    __tablename__ = "books"
    __table_args__ = (UniqueConstraint("id"),)

    def __init__(self, data_dict):
        data_dict = dict(data_dict)
        for key in data_dict:
            lower_key = key.lower()
            setattr(self, lower_key, data_dict[key])

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    publication_year = Column(Integer)
    # reviews = relationship("Reviews", back_populates="book")
