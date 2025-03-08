from fastapi import FastAPI

from product.database import Base, engine
from product.routers import product, login
from product.routers import seller

app = FastAPI(
    title="Products API",
    description="Get details about products",
    terms_of_service="https://www.google.com",
    contact={
        "Developer name": "Pradeep",
        "Website": "https://www.google.com",
        "email": "pradeep@gmail.com"
    },
    license_info={
        "name": "LICENSE",
        "url": "https://www.google.com"
    }
)

app.include_router(product.router)
app.include_router(seller.router)
app.include_router(login.router)

Base.metadata.create_all(engine)
