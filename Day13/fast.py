from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample data storage
items = {}

# Define the structure of an item
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    in_stock: bool = True

# GET
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return items.get(item_id, "Item not found")

# POST
@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    items[item_id] = item
    return item

# PUT
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

# DELETE
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return items.pop(item_id, "Item not found")
