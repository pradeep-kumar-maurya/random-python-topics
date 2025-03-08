from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str


class Seller(BaseModel):
    id: int
    seller_name: str
