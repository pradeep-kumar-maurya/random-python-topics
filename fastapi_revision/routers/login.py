from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.params import Depends
from datetime import datetime, timedelta

from passlib.context import CryptContext
import schemas

from jose import jwt, JWTError

router = APIRouter(tags=['login'])

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

SECRET_KEY = 'ab93a7c9438701bc1f996ff044dc70914237e60252ae772ef1ddf753dce8211a'
ACCESS_TOKEN_EXPIRE_MINUTES = 20
ALORITHM = 'HS256'

'''Note:- tokenUrl must be same as the router of def login method i.e. "login"
because it searches for a route that creates the token'''
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

user_data = {
    'username': 'pradeep',
    'password': '$2b$12$/snU41rAcZGdrtCin8adk.DQDNuH87itA9sEZrSMUgtfxMth621Wq'  # actual passowrd = pradeep123
}


def generate_token(data):
    data_copy = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_copy.update({'exp': expire})
    encoded_jwt_token = jwt.encode(data_copy, SECRET_KEY, ALORITHM)
    return encoded_jwt_token


@router.post("/login", response_model=schemas.Token)
def login(request: OAuth2PasswordRequestForm = Depends()):
    if request.username != user_data.get('username'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not a valid user!!!")
    
    # hashed_pass = pwd_context.hash(request.password)  # to genaret a hashed password
    
    # to verify request password with the already stored hashed password
    if pwd_context.verify(request.password, user_data.get('password')):
        token = generate_token({'user': request.username})
        return {'access_token': token, 'token_type': 'bearer'}
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect Password!')


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid Credentials!!!',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    try:
        jwt_decoded: dict = jwt.decode(token, SECRET_KEY, algorithms=[ALORITHM])
        if jwt_decoded.get('user') is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    

