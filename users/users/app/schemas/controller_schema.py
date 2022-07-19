from uuid import UUID

from pydantic import BaseModel


class UserQuestionnaire(BaseModel):
    user_name: str
    uuid: UUID
    test_1: str
