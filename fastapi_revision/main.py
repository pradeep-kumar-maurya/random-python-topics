from routers import login
from routers import seller
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title = 'FastAPI Demo',
    description = 'This is just for testing'
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

app.include_router(login.router)
app.include_router(seller.router)



@app.get("/")
def hello():
    return {'message': 'hello from FastAPI'}

