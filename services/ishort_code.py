from typing import Protocol
from controllers.models.request.create_short_code import CreateShortCodeRequest
from controllers.models.request.search_short_codes import SearchShortCodesRequest
from controllers.models.response.short_code import ShortCodeCollectionResponse, ShortCodeResponse
from controllers.models.response.short_code_url import ShortCodeURLResponse


class IShortCodeService(Protocol):
    def get_short_code_by_id(self, id: str) -> ShortCodeResponse:
        ...

    def search_short_codes(self, request: SearchShortCodesRequest) -> ShortCodeCollectionResponse:
        ...

    def create_short_code(self, request: CreateShortCodeRequest) -> ShortCodeURLResponse:
        ...
