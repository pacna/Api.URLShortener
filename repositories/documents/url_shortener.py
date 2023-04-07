import datetime
from typing import List
from pymodm import fields, MongoModel
from pymongo import DESCENDING


class URLShortener(MongoModel):
    _id: fields.MongoBaseField = fields.MongoBaseField(primary_key=True)
    url: fields.CharField = fields.CharField(mongo_name="url")
    create_date: fields.DateTimeField = fields.DateTimeField(
        mongo_name="cd")
    counter: fields.IntegerField = fields.IntegerField(mongo_name="c")


class URLShortenerDocument():

    def __init__(self, short_code: str = "", url: str = "", counter: int = 0) -> None:
        self.short_code = short_code
        self.url = url
        self.counter = counter

    def create_document(self) -> None:
        document: URLShortener = URLShortener(
            _id=self.short_code, url=self.url, create_date=datetime.datetime.now(), counter=self.counter)
        document.save()

    def get_document_by_id(self, id: str) -> URLShortener:
        return URLShortener.objects.get({'_id': id})

    def get_document_by_url(self, url: str) -> URLShortener:
        return URLShortener.objects.get({'url': url})

    def search_documents(self, url: str, short_code: str) -> List[URLShortener]:
        filter: dict = self._build_filter(url, short_code)
        query = URLShortener.objects.raw(filter)
        cursor = query.aggregate({'$sort': {'cd': DESCENDING}})
        return list(cursor)

    def get_count(self) -> int:
        return URLShortener.objects.count()

    # protected and private methods
    def _build_filter(self, url: str, short_code: str) -> dict:
        filter: dict = {}

        if url != None:
            filter['url'] = url
        if short_code != None:
            filter['_id'] = short_code

        return filter
