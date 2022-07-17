import json
import os
import uuid

import requests
from fastapi import APIRouter
from fastapi import Request

router = APIRouter(prefix='/users',
                   tags=['users']
                   )


@router.get("/")
def user_base(request: Request):
    _uuid = str(uuid.uuid4())
    body = {"name": "name", "test_1": "value_1", "test_2": "value_2"}
    body = json.dumps(body)
    headers = {
        "accept": "application/json",
        'Content-Type': 'application/json'
    }

    result = requests.post("http://localhost:8000/example", body, headers=headers)
    # result = requests.get("http://localhost:8000")
    print(result.json())
    return {
        "uuid": _uuid,
        "headers": request.headers,
        "path": os.getenv("USER_PATH"),
        "result": result.json()
    }
