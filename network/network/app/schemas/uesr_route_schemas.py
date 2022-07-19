from pydantic import BaseModel


class UserQuestionnaire(BaseModel):
    name: str
    test_1: str
