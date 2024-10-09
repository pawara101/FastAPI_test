from fastapi import FastAPI
from enum import Enum

class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip:int=0,limit:int=0):
    return fake_items_db[skip: skip+limit]

# name = "Pawara"
# @app.get("/")
# async def root():
#     return {f"message": "Hello!!!"}
#
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}
#
#
# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]
