from controllers.models.response.goto import GotoResponse
from repositories.documents.url_shortener import URLShortener
from repositories.url_shortener import URLShortenerRepository

repo: URLShortenerRepository = URLShortenerRepository()


class GotoService():
    def __init__(self) -> None:
        pass

    def get_goto_url(self, code: str) -> GotoResponse:
        document: URLShortener = repo.get_by_id(code)
        response: GotoResponse = GotoResponse(url=document.url)
        return response.dict()
