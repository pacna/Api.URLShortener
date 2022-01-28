from fastapi import APIRouter
from controllers.models.response.goto import GotoResponse
from services.goto import GotoService
from services.igoto import IGotoService

service: IGotoService = GotoService()


class Gotocontrollers:
    router: APIRouter = APIRouter(
        tags=["Goto"],
        prefix="/goto"
    )

    def __init__(self) -> None:
        pass

    @router.get("/{code}", response_model=GotoResponse)
    async def get_goto_url(code: str):
        return service.get_goto_url(code)
