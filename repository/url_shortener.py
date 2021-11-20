import datetime
from pymodm.connection import connect
from controller.models.request.create_short_code import CreateShortCodeRequest
from repository.documents.url_shortener import URLShortenerDocument

connect("mongodb://localhost:27017/url_shortener")


class URLShortenerRepo:
    def add(self, request: CreateShortCodeRequest) -> None:
        URLShortenerDocument("blah", "balh", datetime.datetime.now()).save()
