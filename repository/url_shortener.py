from typing import List
from pymodm.connection import connect
from controller.models.request.search_short_codes import SearchShortCodesRequest
from repository.documents.url_shortener import URLShortener, URLShortenerDocument
from repository.models.url_shortener import URLShortenerModel

connect("mongodb://localhost:27017/url_shortener")


class URLShortenerRepo:
    def __init__(self) -> None:
        self.mongo_counter = 0
        pass

    def add(self, model: URLShortenerModel) -> None:
        URLShortenerDocument(
            url=model.url, short_code=model.short_code, counter=model.counter).create_document()

    def search(self, request: SearchShortCodesRequest) -> List[URLShortener]:
        try:
            return URLShortenerDocument().search_documents(request.url, request.code)
        except Exception as exception:
            print(exception)
            return list(URLShortener())

    def get_by_id(self, id: str) -> URLShortener:
        try:
            return URLShortenerDocument().get_document_by_id(id)
        except Exception as exception:
            print(exception)
            return URLShortener()

    def get_by_short_code(self, short_code: str) -> URLShortener:
        try:
            return URLShortenerDocument().get_document_by_short_code(short_code)
        except Exception as exception:
            print(exception)
            return URLShortener()

    def get_counter(self) -> int:
        if self.mongo_counter == 0:
            self.mongo_counter = URLShortenerDocument().get_count()
            return self.mongo_counter
        else:
            return self.mongo_counter

    def set_counter(self) -> None:
        self.mongo_counter += 1
