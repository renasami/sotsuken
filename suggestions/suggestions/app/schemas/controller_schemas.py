from uuid import UUID

from pydantic import BaseModel


class ClassterdRequest(BaseModel):
    uuid: UUID
