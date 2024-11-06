from fastapi import FastAPI
from enum import Enum
from typing import Union

class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip:int=0,limit:int=0):
    return fake_items_db[skip: skip+limit]

@app.get("/items/{item_id}")
async def read_item_with_path(item_id: str, q:Union[int,None] = None):
    if q:
        return {"item_id":item_id, "q": q}
    return {"item_id":item_id}

@app.get("/users/{user_id}/items/{item_id}") ## http://127.0.0.1:8000/users/1500/items/foo?q=1&short=false
async def read_user_item(
        user_id: int,
        item_id: str,
        q: Union[str,None]=None,
        short:bool = False
):
    item = {"item_id":item_id, "owner_id":user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/needy/{item_id}")
async def read_needy_items(item_id:str,must:str):
    item = {"item_id":item_id,"must":must}
    return item


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
