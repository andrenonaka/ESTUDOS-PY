from typing import Union
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/teste/{name}", response_class=HTMLResponse)
def read_items(name:str):
    return f"""
    html>
        <head>
            <title>Some HTML in here </title>
        </head>
        <boy>
            <s2>Look ma! HTML! {name}</h1>
        </body>
    </html>
    """