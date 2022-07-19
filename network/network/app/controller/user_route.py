import json
import os
import uuid

import requests
from fastapi import APIRouter
from fastapi import Request

from network.app.schemas.uesr_route_schemas import UserQuestionnaire
from network.app.util.generator import RandomNumberGenerator, EventGenerator
from network.app.util.observer import DigitObserver, GraphObserver, SuggestionedObserver

router = APIRouter(prefix='/users',
                   tags=['users']
                   )

event_list = []


@router.post("/")
def user_base(request: Request, body: UserQuestionnaire):
    _uuid = str(uuid.uuid4())
    body = {"user_name": body.name, "uuid": _uuid, "test_1": body.test_1}
    body = json.dumps(body)
    headers = {
        "accept": "application/json",
        'Content-Type': 'application/json'
    }

    result = requests.post("http://localhost:8000/example", body, headers=headers)
    print(result.json())
    if result.json()["uuid"] == _uuid:
        return True
    return {
        "uuid": _uuid,
        "headers": request.headers,
        "path": os.getenv("USER_PATH"),
        "result": result.json()
    }


@router.get("/")
def generator_test():
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    generator.execute()


@router.get("/test")
def test():
    generator = EventGenerator()
    event_list.append(generator.get_uuid())
    for _ in range(10):
        # EventGenerator().add_observer()
        event_list.append(EventGenerator().get_uuid())
    print(event_list)
    observer = SuggestionedObserver(generator.get_uuid())
    generator.add_observer(observer)
    generator.execute()
    requests.get("http://localhost:8888/test")
