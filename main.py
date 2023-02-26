from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id:int
    name:str
    email:str
    city:str
    state:str
    pincode:int
    status:bool=True


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None): #Union[str, None] means either str or none and optional too i.e Optional[X] as a shorthand for Union[X, None]
    return {"item_id": item_id, "q": q}


# @app.get("/test/{no}")
# def test_fun(no : int, p: Union[str, None]=None):
#     return {'number':no,'params':p}

@app.put("/user/{user_id}")
def update_user(user_id:int, user:User):
    return {"user_name":user.name, "id":user_id}
