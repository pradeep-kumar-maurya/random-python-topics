from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from product import models
from product.database import get_db
from product.routers.login import get_current_user
from product.schemas import Product, ProductResponseModel, Seller

router = APIRouter(tags=['Products'], prefix="/product")


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_product(request: Product, db: Session = Depends(get_db)):
    new_product = models.Product(name=request.name,
                                 description=request.description,
                                 price=request.price,
                                 seller_id=request.seller_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request


# this route is protected by OAuth2
@router.get("/")
def get_all_products(db: Session = Depends(get_db), current_user: Seller = Depends(get_current_user)):
    products = db.query(models.Product).all()
    return products


# this route is protected by OAuth2
@router.get("/{id}", response_model=ProductResponseModel)
def get_product_by_id(id: int, db: Session = Depends(get_db), current_user: Seller = Depends(get_current_user)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found!")
    return product

# similarly try delete and update to the DB
