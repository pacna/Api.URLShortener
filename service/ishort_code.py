from controller.models.request.create_short_code import CreateShortCodeRequest
from controller.models.request.search_short_codes import SearchShortCodesRequest
from controller.models.response.short_code import ShortCodeCollectionResponse, ShortCodeResponse
from controller.models.response.short_code_url import ShortCodeURLResponse


class IShortCodeService:
    def get_short_code_by_id(self, id: str) -> ShortCodeResponse:
        pass

    def search_short_codes(self, request: SearchShortCodesRequest) -> ShortCodeCollectionResponse:
        pass

    def create_short_code(self, request: CreateShortCodeRequest) -> ShortCodeURLResponse:
        pass
