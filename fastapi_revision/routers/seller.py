from fastapi import APIRouter, HTTPException, status, Form
from fastapi.params import Depends
from .login import get_current_user
import schemas

router = APIRouter(tags=['Seller'])


seller_data = {
    1: 'seller 1',
    2: 'seller 2'
}


@router.post("/addSeller")
def add_seller(request: schemas.Seller, current_user = Depends(get_current_user)):
    '''
    curl -X 'POST' \
    'http://127.0.0.1:8000/addSeller' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoicHJhZGVlcCIsImV4cCI6MTc0MTI5MTg3NH0.ujzlw3zddoQgJsFTkGB7-nHNCmeLliZ9u-TSvyp-OOM' \
    -H 'Content-Type: application/json' \
    -d '{
    "id": 3,
    "seller_name": "seller 3"
    }'
    '''
    seller_data[request.id] = request.seller_name
    return seller_data


@router.get("/getSeller/{id}/{batch}", response_model=schemas.Seller)
def get_seller(id: int, batch: int, seller_name: str, seller_address: str, current_user=Depends(get_current_user)):
    # URL = http://127.0.0.1:8000/getSeller/1/2025?seller_name=seller%201&seller_address=hyd
    if seller_data.get(id):
        return seller_data.get(id)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid seller id!!!')
    

@router.post("/email")
def email(username: str = Form(...), password: str = Form(...)):
    '''
    curl -X 'POST' \
    'http://127.0.0.1:8000/email' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'username=pradeep&password=pradeep123'
    '''
    return {'username': username, 'password': password}
    

