from fastapi import FastAPI, Header, Response, HTTPException
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

# Fake database
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Data model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []

# Basic static path
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Path parameters
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id, "times_two": str(int(item_id) * 2)}


@app.get("/items/{item_id}/configs/{config_id}")
async def read_item(item_id, config_id):
    return {
        "item_id": item_id,
        "times_two": str(int(item_id) * 2),
        "config_id": config_id,
    }


# Path with query
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# Headers parameters
@app.get("/foods/")
async def read_foods(
    user_agent: Optional[str] = Header(None),
    my_token: Optional[str] = Header(None),
):
    return {"User-Agent": user_agent, "My-Token": my_token}


# CREATE item
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


# DELETE item
# also better docummentation and response codes
@app.delete(
    "/items/{item_id}",
    summary="Delete an awesome item",
    response_class=Response,
    responses={
        200: {"description": "Item successfully deleted"},
        404: {"description": "Item not found"},
    },
)
async def delete_item(item_id: int):
    if item_id == 69:
        raise HTTPException(
            status_code=404,
            detail="Item not found. Already of stock for obvious reasons.",
            headers={"X-Error": "Already of stock for obvious reasons."},
        )

    return item_id

# UPDATE item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    return item
