from fastapi import FastAPI, Header
from typing import Optional

app = FastAPI()

# Fake database
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

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

