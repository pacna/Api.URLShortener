from dotenv import dotenv_values

config = dotenv_values('.env')


class ENVHelper:
    def __init__(self) -> None:
        pass

    def get_host(self) -> str:
        try:
            return config.get('HOST')
        except:
            return ''

    def get_mongo_uri(self) -> str:
        try:
            return config.get('MONGO_URI')
        except:
            return ''
