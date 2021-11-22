class URLShortenerModel:
    def __init__(self, url: str, short_code: str, counter: int) -> None:
        self.url = url
        self.short_code = short_code
        self.counter = counter
