from controller.models.response.goto import GotoResponse
from service.igoto import IGotoService


class TestGotoService(IGotoService):
    def get_goto_url(self, code: str) -> GotoResponse:
        return GotoResponse(url='http://www.google.com')
