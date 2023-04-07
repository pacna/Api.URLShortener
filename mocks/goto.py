from controllers.models.response.goto import GotoResponse


class TestGotoService():
    def get_goto_url(self, code: str) -> GotoResponse:
        return GotoResponse(url='http://www.google.com')
