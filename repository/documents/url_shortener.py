import datetime
from typing import List
from pymodm import fields, MongoModel
from bson.objectid import ObjectId
from pymongo import DESCENDING


class URLShortener(MongoModel):
    short_code: fields.CharField = fields.CharField(mongo_name="sc")
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
            self.short_code, self.url, datetime.datetime.now(), self.counter)
        document.save()

    def get_document_by_id(self, id: str) -> URLShortener:
        return URLShortener.objects.get({'_id': ObjectId(id)})

    def get_document_by_url(self, url: str) -> URLShortener:
        return URLShortener.objects.get({'url': url})

    def get_document_by_short_code(self, short_code: str) -> URLShortener:
        return URLShortener.objects.get({'sc': short_code})

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
            filter['sc'] = short_code

        return filter
