from fastapi import APIRouter, Body, Depends
from schema.user import UserSchema, UserLoginSchema
from auth.auth_handler import signJWT
from services.user import UserService, UserDataManager
from sqlalchemy.orm import Session
from backend.session import create_session

router = APIRouter()

users = []


def check_user(data: UserLoginSchema, session):
    user = UserDataManager(session).get_user(data)
    if user and (user.email == data.email and user.password == data.password):
        return True
    return False


@router.post("/user/signup", tags=["user"])
async def create_user(
    user: UserSchema = Body(...), session: Session = Depends(create_session)
):
    users.append(user)

    token = signJWT(user.email)
    if token:
        UserService(session).convert_data_into_obj(user)
        return token


@router.post("/user/login", tags=["user"])
async def user_login(
    user: UserLoginSchema = Body(...),
    session: Session = Depends(create_session),
):
    if check_user(user, session):
        return signJWT(user.email)
    return {"error": "Wrong login details!"}
