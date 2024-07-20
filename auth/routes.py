from fastapi import Body, APIRouter, Depends
from typing import Optional
from starlette.requests import Request
from .models import *
from .functions.jwt_bearer import JWTBearer
from .abstract import abstract_func
from fastapi.security import HTTPBasicCredentials


router = APIRouter()


@router.post("/login")
def login_route(credentials: HTTPBasicCredentials = Body(...)):
    return abstract_func('user_login', credentials)


@router.post("/signup")
def signup_route(data: SignUpModel = Body(...)):
    return abstract_func('user_signup', data)


@router.get('/profile', dependencies=[Depends(JWTBearer(auto_error=False))])
async def get_profile_route(request: Request):
    return abstract_func('get_profile', request)