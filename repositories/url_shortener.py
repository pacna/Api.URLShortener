from typing import List
from pymodm.connection import connect
from controllers.models.request.search_short_codes import SearchShortCodesRequest
from repositories.documents.url_shortener import URLShortener, URLShortenerDocument
from services.helpers.env import ENVHelper

config: ENVHelper = ENVHelper()

connect(f"{config.get_mongo_uri()}/url_shortener")


class URLShortenerRepository:
    def __init__(self) -> None:
        self.mongo_cache_counter = 0

    def add(self, doc: URLShortenerDocument) -> None:
        doc.create_document()

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

    def get_by_url(self, url: str) -> URLShortener:
        try:
            return URLShortenerDocument().get_document_by_url(url)
        except Exception as exception:
            print(exception)
            return URLShortener()

    def get_counter(self) -> int:
        if self.mongo_cache_counter == 0:
            self.mongo_cache_counter = URLShortenerDocument().get_count()
            return self.mongo_cache_counter
        else:
            return self.mongo_cache_counter

    def set_counter(self) -> None:
        self.mongo_cache_counter += 1
