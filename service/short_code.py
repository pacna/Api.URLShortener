from controller.models.request.create_short_code import CreateShortCodeRequest
from controller.models.response.short_code import ShortCodeResponse
from repository.documents.url_shortener import URLShortener
from repository.url_shortener import URLShortenerRepo

repo: URLShortenerRepo = URLShortenerRepo()


class ShortCodeService:
    def __init__(self) -> None:
        pass

    def create_short_code(self, request: CreateShortCodeRequest) -> None:
        repo.add(request)

    def get_short_code(self, id: str) -> ShortCodeResponse:
        document: URLShortener = repo.get(id)
        response: ShortCodeResponse = ShortCodeResponse(
            url=document.url, short_code=document.short_code)
        return response.dict()
