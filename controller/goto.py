from fastapi import APIRouter
from controller.models.response.goto import GotoResponse


class GotoController:
    router: APIRouter = APIRouter(
        tags=["Goto"],
        prefix="/goto"
    )

    def __init__(self) -> None:
        pass

    @router.get("/{url}", response_model=GotoResponse)
    async def get_goto_url(url: str):
        response = GotoResponse(url="blah")
        return response.dict()
