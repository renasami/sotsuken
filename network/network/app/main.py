from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .controller import user_route, handler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/auth/register")
def register():
    print("hello")


@app.get("/test")
def test():
    return {"Hello": "World"}


app.include_router(user_route.router)
app.include_router(handler.router)


def main():
    uvicorn.run("network.main:main", host="0.0.0.0", port=8080, reload=True)
