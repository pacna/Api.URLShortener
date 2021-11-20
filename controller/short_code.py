from fastapi import APIRouter, status, Response
from controller.models.request.create_short_code import CreateShortCodeRequest
from service.short_code import ShortCodeService
from .models.request.create_short_code import CreateShortCodeRequest
from .models.response.short_code import ShortCodeCollectionResponse, ShortCodeResponse

service: ShortCodeService = ShortCodeService()


class ShortCodeController:
    router: APIRouter = APIRouter(
        tags=["Short Code"],
        prefix="/short-code"
    )

    def __init__(self) -> None:
        pass

    @router.get("", response_model=ShortCodeCollectionResponse)
    async def search_short_codes(code: str, url: str):
        return "blah"

    @router.get("/{id}", response_model=ShortCodeResponse)
    async def get_short_code(id: str):
        return service.get_short_code(id)

    @router.post("", status_code=status.HTTP_201_CREATED)
    async def create_short_code(request: CreateShortCodeRequest, response: Response):
        service.create_short_code(request)
        response.status_code = status.HTTP_201_CREATED
        return response
