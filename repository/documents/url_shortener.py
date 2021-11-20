from pymodm import fields, MongoModel


class URLShortenerDocument(MongoModel):
    short_code: fields.CharField = fields.CharField()
    url: fields.CharField = fields.CharField()
    create_date: fields.DateTimeField = fields.DateTimeField()
