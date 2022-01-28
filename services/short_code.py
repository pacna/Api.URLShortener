from typing import List
from fastapi import HTTPException, status
from controllers.models.request.create_short_code import CreateShortCodeRequest
from controllers.models.request.search_short_codes import SearchShortCodesRequest
from controllers.models.response.short_code import ShortCodeCollectionResponse, ShortCodeResponse
from controllers.models.response.short_code_url import ShortCodeURLResponse
from repositories.documents.url_shortener import URLShortener, URLShortenerDocument
from repositories.url_shortener import URLShortenerRepository
from validators import url
from services.helpers.hash import HashHelper
from services.helpers.env import ENVHelper
from services.ishort_code import IShortCodeService
from services.models.validation import ValidationModel

repo: URLShortenerRepository = URLShortenerRepository()


class ShortCodeService(IShortCodeService):
    def __init__(self) -> None:
        super().__init__()

    def create_short_code(self, request: CreateShortCodeRequest) -> ShortCodeURLResponse:
        validation: ValidationModel = self._check_validation(request.url)
        if (not validation.is_error):
            counter: int = repo.get_counter()
            hash: str = HashHelper(counter=counter).create_hash()
            doc: URLShortenerDocument = URLShortenerDocument(
                url=request.url, short_code=hash, counter=counter)
            repo.add(doc)
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
