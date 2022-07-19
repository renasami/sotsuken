from fastapi import APIRouter

from network.app.schemas.handler_schema import Suggestioned

router = APIRouter(prefix='/event_handler',
                   tags=['event_handler']
                   )


@router.post("/suggestioned")
def suggestiond(body: Suggestioned):
    pass