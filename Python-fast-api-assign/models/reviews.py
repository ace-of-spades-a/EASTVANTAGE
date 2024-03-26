from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship, registry
from models.base import BASE

mapper_registry = registry()


class Reviews(BASE):
    __tablename__ = "reviews"
    __table_args__ = (UniqueConstraint("review_id"),)

    def __init__(self, data_dict):
        data_dict = dict(data_dict)
        for key in data_dict:
            lower_key = key.lower()
            setattr(self, lower_key, data_dict[key])

    review_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(
        Integer, ForeignKey("books.id")
    )  # Foreign key referencing books table
    text = Column(String)
    rating = Column(Integer)

    # Establishing a relationship with the Book model
    # book = relationship("Book", back_populates="review")
