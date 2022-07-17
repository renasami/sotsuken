from typing import Optional

from fastapi import FastAPI,APIRouter
from fastapi.middleware.cors import CORSMiddleware
import controller.user_route as user_route


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



prefix = APIRouter(prefix="/api/v1")


# app.include_router(prefix)

# @prefix.get('/prefix')
# def prefix():
    # return "prefix"

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

