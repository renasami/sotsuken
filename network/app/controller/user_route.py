from fastapi import APIRouter
import uuid
from fastapi import Request
from typing import Union
import requests
import os


router = APIRouter(prefix='/users',
    tags=['users']
)


@router.get("/")
def user_base(request: Request):
    _uuid = str(uuid.uuid4())
    
    return {
        "uuid": _uuid,
        "headers":request.headers,
        "path":os.getenv("USER_PATH")
    }