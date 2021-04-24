from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id, "times_two": str(int(item_id)*2)}

@app.get("/items/{item_id}/configs/{config_id}")
async def read_item(item_id, config_id):
    return {"item_id": item_id, "times_two": str(int(item_id)*2), "config_id": config_id}
