from typing import List
from fastapi import HTTPException, status
from controller.models.request.create_short_code import CreateShortCodeRequest
from controller.models.request.search_short_codes import SearchShortCodesRequest
from controller.models.response.short_code import ShortCodeCollectionResponse, ShortCodeResponse
from repository.documents.url_shortener import URLShortener
from repository.models.url_shortener import URLShortenerModel
from repository.url_shortener import URLShortenerRepo
from validators import url

repo: URLShortenerRepo = URLShortenerRepo()


class ShortCodeService:
    def __init__(self) -> None:
        pass

    def create_short_code(self, request: CreateShortCodeRequest) -> None:
        if (self._is_valid_url(request.url)):
            counter: int = repo.get_counter()
            model: URLShortenerModel = URLShortenerModel(
                url=request.url, short_code='blah', counter=counter)
            repo.add(model)
            repo.set_counter()
        else:
            raise HTTPException(
                status_code=status.HTTP_412_PRECONDITION_FAILED, detail="email is invalid")

    def search_short_codes(self, request: SearchShortCodesRequest) -> ShortCodeCollectionResponse:
        documents: List[URLShortener] = repo.search(request)
        response: ShortCodeCollectionResponse = self._map_document_to_response(
            documents)
        return response

    def get_short_code_by_id(self, id: str) -> ShortCodeResponse:
        document: URLShortener = repo.get_by_id(id)
        response: ShortCodeResponse = ShortCodeResponse(
            url=document.url, short_code=document.short_code, id=str(document._id))
        return response.dict()

    # private and protected methods
    def _map_document_to_response(self, documents: List[
            URLShortener]) -> ShortCodeCollectionResponse:
        response_list: List[ShortCodeResponse] = []

        for doc in documents:
            response: ShortCodeResponse = ShortCodeResponse(
                url=doc['url'], short_code=doc['sc'], id=str(doc['_id']))
            response_list.append(response)

        response: ShortCodeCollectionResponse = ShortCodeCollectionResponse(
            list=response_list, count=len(response_list))

        return response

    def _is_valid_url(self, request_url: str) -> bool:
        valid = url(request_url)

        return valid == True
