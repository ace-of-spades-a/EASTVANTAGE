from fastapi import APIRouter, Depends, status, Response, Path
from sqlalchemy.orm import Session
from backend.session import create_session
from pydantic import BaseModel
from services.books import BookService, BookDataManager
from models.books import Book

router = APIRouter()


class BookInput(BaseModel):
    title: str
    author: str
    publication_year: int


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    publication_year: int


@router.post("/book", status_code=status.HTTP_201_CREATED)
def add_book(
    book: BookInput, res: Response, session: Session = (Depends(create_session))
):
    """Accepting the json data which validate from pydentic BookInput Class"""
    try:
        res = BookService(session).convert_data_into_obj(book)
        session.query(Book).filter(Book.id)
    except Exception as e:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {"Error": str(e)}
    return {"Success": "Book Added", "Data": res}


@router.get(
    "/book/{book_id}",
    response_model=BookResponse | dict,
    status_code=status.HTTP_200_OK,
)
def get_book(
    res: Response,
    book_id: int = Path(..., title="The ID of the book to retrieve"),
    session: Session = Depends(create_session),
):
    if book_id and isinstance(book_id, int):
        book = fetch_book_from_DB(book_id, session)
        if book:
            return book
        else:
            res.status_code = status.HTTP_404_NOT_FOUND
            return {"Error": "Ops! Invalid Book Id."}


def fetch_book_from_DB(book_id: int, session: Session):
    return BookDataManager(session).get_book(book_id)
