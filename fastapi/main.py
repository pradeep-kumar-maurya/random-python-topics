from enum import Enum
from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel, Field

app = FastAPI()


class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    # Field is used to define the metadata for a particular attribute in the pydantic model
    name: str = Field(example="drill machine",
                      title="name of the tool",
                      description="this is the name of the tool to be added")
    price: float
    count: int = Field(ge=0)
    id: int
    category: Category = Field(example="Enum -> tools | consumables")


items = {
    0: Item(name="hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="pliers", price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name="nails", price=1.99, count=100, id=2, category=Category.CONSUMABLES)
}

# TODO - Note:- static API routes must be placed before the dynamic routes to avoid ambiguity


@app.get("/items")
def index():
    return {"items": items}


# item_id is a path parameter here because it's available in the URL path and is provided to the function as a parameter
@app.get("/items/{item_id}")
def query_item(item_id: int) -> Item:
    if items.get(item_id) is None:
        raise HTTPException(status_code=404, detail=f"there is no item with item_id = {item_id}")
    return items[item_id]


# GET: example for query parameters
@app.get("/items/")
def query_items_by_parameters(name: str = None, price: float = None, count: int = None, category: Category = None):
    def check_item(item: Item) -> bool:
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category
            )
        )

    data = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "fetched_data": data
    }


# GET: path + query parameters
@app.get("/items/{item_id}/information")
def process_item_info(item_id: int, name: str):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail=f"There is no item if item id: {item_id}")
    if item.name == name:
        return item
    else:
        return f"There is no item if item id: {item_id} and name: {name}"


# POST method
@app.post("/addItem")
def add_item(item: Item):
    if items.get(item.id):
        raise HTTPException(status_code=409, detail=f"An item already exist with item id: {item.id}")
    items[item.id] = item
    return {
        "details": f"Item added with item id: {item.id}",
        "items": items
    }


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
