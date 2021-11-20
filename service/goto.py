from controller.models.response.goto import GotoResponse
from repository.url_shortener import URLShortenerRepo


repo: URLShortenerRepo = URLShortenerRepo()


class GotoService:
    def __init__(self) -> None:
        pass

    def get_goto_url(self, url: str) -> GotoResponse:
        return GotoResponse(url="Blah").dict()
