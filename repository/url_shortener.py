from pymodm.connection import connect
from controller.models.request.create_short_code import CreateShortCodeRequest
from repository.documents.url_shortener import URLShortener, URLShortenerDocument

connect("mongodb://localhost:27017/url_shortener")


class URLShortenerRepo:
    def add(self, request: CreateShortCodeRequest) -> None:
        URLShortenerDocument("blah", "balh").create_document()

    def get(self, id: str) -> URLShortener:
        try:
            return URLShortenerDocument().get_document(id)
        except Exception as exception:
            print(exception)
            return URLShortener()
