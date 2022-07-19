import json
from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from suggestions.app.schemas.controller_schemas import ClassterdRequest

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


@app.post("/post")
def post(body: ClassterdRequest):
    body = {"uuid": body.uuid}
    body = json.dumps(body)
    headers = {
        "accept": "application/json",
        'Content-Type': 'application/json'
    }
    # result = requests.post("http://localhost:8080", body, headers=headers)
    return body


def main():
    uvicorn.run("suggestions.main:main", host="0.0.0.0", port=8888, reload=True)


if __name__ == "__main__":
    main()
