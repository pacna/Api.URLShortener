from controllers.models.response.goto import GotoResponse
from repositories.documents.url_shortener import URLShortener
from repositories.url_shortener import URLShortenerRepository
from services.igoto import IGotoService


repo: URLShortenerRepository = URLShortenerRepository()


class GotoService(IGotoService):
    def __init__(self) -> None:
        super().__init__()

    def get_goto_url(self, code: str) -> GotoResponse:
        document: URLShortener = repo.get_by_short_code(code)
        response: GotoResponse = GotoResponse(url=document.url)
        return response.dict()
