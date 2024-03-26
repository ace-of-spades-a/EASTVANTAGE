from fastapi import APIRouter, Depends, status, Response, Path
from sqlalchemy.orm import Session
from backend.session import create_session
import pydantic
from typing import Optional

# from routers.books import fetch_book_from_DB
from services.reviews import ReviewService
from backend.config import settings
import requests
from models.books import Book
from models.reviews import Reviews
from services.reviews import ReviewDataManager

router = APIRouter()


class ReviewInput(pydantic.BaseModel):
    text: str
    rating: int


@router.post("/review/{book_id}", status_code=status.HTTP_201_CREATED)
def add_review(
    review: ReviewInput,
    res: Response,
    book_id=Path(..., title=""),
    session: Session = Depends(create_session),
):
    book_res = requests.get(f"{settings.BASE_URL}/book/{book_id}")
    if book_res:
        review = review.model_dump()
        review.update({"book_id": book_res.json().get("id")})
        res = ReviewService(session).convert_data_into_obj(review)
        return res
    else:
        res.status_code = status.HTTP_404_NOT_FOUND
        return {"Erro": "Invalid Book ID."}


@router.get("/reviews", status_code=status.HTTP_200_OK)
def listout_reviews(
    res: Response,
    author: Optional[str] = None,
    publish_year: Optional[int] = None,
    session: Session = Depends(create_session),
):
    if not author and not publish_year:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": "please provide author or publish year"}
    Books = None

    if author:
        Books = session.query(Book).filter(Book.author == author)

    if publish_year:
        Books = session.query(Book).filter(
            Book.publication_year == publish_year
        )
    reviews = []
    if Books:
        ids = [book.id for book in Books]
        for id in ids:
            res_reviews = ReviewDataManager(session).get_all(
                session.query(Reviews).filter(Reviews.book_id == id)
            )
            [reviews.append(res) for res in res_reviews]

    return reviews
