from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from product import models
from product.database import get_db
from product.schemas import Seller, SellerResponseModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(tags=['Seller'])


@router.post("/add_seller", response_model=SellerResponseModel)
def add_seller(request: Seller, db: Session = Depends(get_db)):
    # create a hash out of the password
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(username=request.username, email=request.email, password=hashed_password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
