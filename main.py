from typing import Optional

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
#from fastapi.staticfiles import StaticFiles
#from fastapi.templating import Jinja2Templates

app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")
#template = Jinja2Templates(directory="./templates")
origins = [
    "http://wec.org.ng",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

###############################
