from typing import List
from controller.models.request.create_short_code import CreateShortCodeRequest
from controller.models.request.search_short_codes import SearchShortCodesRequest
from controller.models.response.short_code import ShortCodeCollectionResponse, ShortCodeResponse
from controller.models.response.short_code_url import ShortCodeURLResponse
from service.short_code import IShortCodeService


class TestShortService(IShortCodeService):
    def get_short_code_by_id(self, id: str) -> ShortCodeResponse:
        return ShortCodeResponse(url='http://www.google.com', short_code="ww", id=id)

    def search_short_codes(self, request: SearchShortCodesRequest) -> ShortCodeCollectionResponse:
        mock_list: List[ShortCodeResponse] = [ShortCodeResponse(
            url=request.url, short_code=request.code, id='test1')]
        return ShortCodeCollectionResponse(list=mock_list, count=1)

    def create_short_code(self, request: CreateShortCodeRequest) -> ShortCodeURLResponse:
        return ShortCodeURLResponse(url="http://www.pacna.com/goto/blah")
