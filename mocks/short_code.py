from typing import List
from controllers.models.request.create_short_code import CreateShortCodeRequest
from controllers.models.request.search_short_codes import SearchShortCodesRequest
from controllers.models.response.short_code import ShortCodeCollectionResponse, ShortCodeResponse
from controllers.models.response.short_code_url import ShortCodeURLResponse


class TestShortService():
    def get_short_code_by_id(self, id: str) -> ShortCodeResponse:
        return ShortCodeResponse(url='http://www.google.com', id=id)

    def search_short_codes(self, request: SearchShortCodesRequest) -> ShortCodeCollectionResponse:
        mock_list: List[ShortCodeResponse] = [ShortCodeResponse(
            url=request.url, id=request.code)]
        return ShortCodeCollectionResponse(list=mock_list, count=1)

    def create_short_code(self, request: CreateShortCodeRequest) -> ShortCodeURLResponse:
        return ShortCodeURLResponse(url="http://www.pacna.com/goto/blah")
