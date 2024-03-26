from fastapi import FastAPI
from models.base import BASE
from backend.session import engin, settings
from routers.books import router as book_route
from routers.reviews import router as review_route

BASE.metadata.create_all(bind=engin)
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="",
    version="1.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)
print("Main running...")
app.include_router(book_route)
app.include_router(review_route)
