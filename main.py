from typing import Optional

from fastapi import FastAPI

#from fastapi.staticfiles import StaticFiles
#from fastapi.templating import Jinja2Templates

app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")
#template = Jinja2Templates(directory="./templates")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

###############################
