from fastapi import APIRouter
from controller.models.response.goto import GotoResponse
from service.goto import GotoService
from service.igoto import IGotoService

service: IGotoService = GotoService()


class GotoController:
    router: APIRouter = APIRouter(
        tags=["Goto"],
        prefix="/goto"
    )

    def __init__(self) -> None:
        pass

    @router.get("/{code}", response_model=GotoResponse)
    async def get_goto_url(code: str):
        return service.get_goto_url(code)
