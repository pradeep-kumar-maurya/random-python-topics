from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: int
    seller_id: int


class SellerResponseModel(BaseModel):
    username: str
    email: str

    class Confid:
        orm_mode = True


class ProductResponseModel(BaseModel):
    name: str
    description: str
    seller: SellerResponseModel

    class Config:
        orm_mode = True


class Seller(BaseModel):
    username: str
    email: str
    password: str


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str]
