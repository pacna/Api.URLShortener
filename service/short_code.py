from typing import List
from fastapi import HTTPException, status
from controller.models.request.create_short_code import CreateShortCodeRequest
from controller.models.request.search_short_codes import SearchShortCodesRequest
from controller.models.response.short_code import ShortCodeCollectionResponse, ShortCodeResponse
from controller.models.response.short_code_url import ShortCodeURLResponse
from repository.documents.url_shortener import URLShortener
from repository.models.url_shortener import URLShortenerModel
from repository.url_shortener import URLShortenerRepo
from validators import url
from service.helper.hash import HashHelper
from service.helper.env import ENVHelper
from service.models.validation import ValidationModel

repo: URLShortenerRepo = URLShortenerRepo()


class ShortCodeService:
    def __init__(self) -> None:
        pass

    def create_short_code(self, request: CreateShortCodeRequest) -> ShortCodeURLResponse:
        validation: ValidationModel = self._check_validation(request.url)
        if (not validation.is_error):
            counter: int = repo.get_counter()
            hash: str = HashHelper(counter=counter).create_hash()
            model: URLShortenerModel = URLShortenerModel(
                url=request.url, short_code=hash, counter=counter)
            repo.add(model)
            repo.set_counter()

            tiny_url: str = self._create_tiny_url(hash)

            return ShortCodeURLResponse(url=tiny_url).dict()
        else:
            raise HTTPException(
                status_code=status.HTTP_412_PRECONDITION_FAILED, detail=validation.error_msg)

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

    def _does_url_exist_in_mongo(self, url: str) -> bool:
        document: URLShortener = repo.get_by_url(url)
        return document.url is not None

    def _is_valid_url(self, request_url: str) -> bool:
        valid = url(request_url)

        return valid == True

    def _check_validation(self, request_url: str) -> ValidationModel:
        if not self._is_valid_url(request_url):
            return ValidationModel(is_error=True, error_msg="Url is invalid")
        elif self._does_url_exist_in_mongo(request_url):
            return ValidationModel(is_error=True, error_msg="Url already exist in mongo")
        else:
            return ValidationModel(is_error=False, error_msg="")

    def _create_tiny_url(self, short_code: str) -> str:
        host: str = ENVHelper().get_host()

        if host == 'localhost':
            return f'http://{host}:8000/goto/{short_code}'

        return f'http://{host}/goto/{short_code}'
