from fastapi import FastAPI
from routers.user import router as user_router
from routers.address import router as address_router
from models.base import BASE
from backend.session import engine, settings

BASE.metadata.create_all(bind=engine)
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="",
    version="1.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)
app.include_router(user_router)
app.include_router(address_router)
