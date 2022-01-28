from typing import Optional
from fastapi import APIRouter
from controllers.models.request.create_short_code import CreateShortCodeRequest
from controllers.models.request.search_short_codes import SearchShortCodesRequest
from controllers.models.response.short_code_url import ShortCodeURLResponse
from services.ishort_code import IShortCodeService
from services.short_code import ShortCodeService
from .models.request.create_short_code import CreateShortCodeRequest
from .models.response.short_code import ShortCodeCollectionResponse, ShortCodeResponse

service: IShortCodeService = ShortCodeService()


class ShortCodeController:
    router: APIRouter = APIRouter(
        tags=["Short Code"],
        prefix="/short-code"
    )

    def __init__(self) -> None:
        pass

    @router.get("", response_model=ShortCodeCollectionResponse)
    async def search_short_codes(code: Optional[str] = None, url: Optional[str] = None):
        request: SearchShortCodesRequest = SearchShortCodesRequest(url, code)
        return service.search_short_codes(request)

    @router.get("/{id}", response_model=ShortCodeResponse)
    async def get_short_code(id: str):
        return service.get_short_code_by_id(id)

    @router.post("", response_model=ShortCodeURLResponse)
    async def create_short_code(request: CreateShortCodeRequest):
        response: ShortCodeURLResponse = service.create_short_code(request)
        return response
