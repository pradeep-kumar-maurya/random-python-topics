from datetime import datetime, timedelta
from typing import List

from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.params import Depends
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from product.database import get_db
from product.models import Seller
from product.schemas import Login, TokenData

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "e6fbfa99c7aa0023ca2146f0c90a72a0bebd157327c12557f7ba5fdc52fc592d"  # openssl rand -hex 32 (git bash command)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

# tokenUrl is the .py file which contains the code for generating the token which is login.py file in our case.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

router = APIRouter(
    tags=['login']
)


# Generate the JWT token for a user
def generate_toke(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    sellers: List[Seller] = db.query(Seller).filter(Seller.username == request.username).all()
    if not sellers:
        raise HTTPException(status_code=404, detail="No user found!")
    for seller in sellers:
        # verify the hashed password from DB with the password from request
        if pwd_context.verify(request.password, seller.password):
            access_token = generate_toke(
                # username is stored in the 'sub' key
                data={'sub': seller.username}
            )
            return {'access_token': access_token, 'token_type': 'bearer'}
    raise HTTPException(status_code=404, detail="Incorrect Password!")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid auth credentials",
            headers={'WWW-Authenticate': 'Bearer'}
        )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # username was stored in the 'sub' key during creation of JWT token
        username = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
