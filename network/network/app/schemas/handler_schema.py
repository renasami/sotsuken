from uuid import UUID

from pydantic import BaseModel


class Suggestioned(BaseModel):
    uuid: UUID
