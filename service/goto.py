from controller.models.response.goto import GotoResponse
from repository.documents.url_shortener import URLShortener
from repository.url_shortener import URLShortenerRepo


repo: URLShortenerRepo = URLShortenerRepo()


class GotoService:
    def __init__(self) -> None:
        pass

    def get_goto_url(self, code: str) -> GotoResponse:
        document: URLShortener = repo.get_by_short_code(code)
        response: GotoResponse = GotoResponse(url=document.url)
        return response.dict()
