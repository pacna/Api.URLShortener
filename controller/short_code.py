from fastapi import APIRouter
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

    @router.get("/{code}", response_model=ShortCodeResponse)
    async def get_short_code(code: str):
        response = ShortCodeResponse(
            url="foobar", short_code="blah blah")
        return response.dict()

    @router.post("")
    async def create_short_code(request: CreateShortCodeRequest):
        return service.create_short_code(request)
