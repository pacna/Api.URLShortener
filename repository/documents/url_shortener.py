import datetime
from pymodm import fields, MongoModel
from bson.objectid import ObjectId


class URLShortener(MongoModel):
    short_code: fields.CharField = fields.CharField(mongo_name="sc")
    url: fields.CharField = fields.CharField(mongo_name="url")
    create_date: fields.DateTimeField = fields.DateTimeField(
        mongo_name="cd")


class URLShortenerDocument():

    def __init__(self, short_code: str = '', url: str = '') -> None:
        self.short_code = short_code
        self.url = url

    def create_document(self) -> None:
        document: URLShortener = URLShortener(
            self.short_code, self.url, datetime.datetime.now())
        document.save()

    def get_document(self, id: str) -> URLShortener:
        return URLShortener.objects.get({'_id': ObjectId(id)})

    def get_count(self) -> int:
        return URLShortener.objects.count()
