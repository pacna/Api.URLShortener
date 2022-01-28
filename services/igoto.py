from controllers.models.response.goto import GotoResponse


class IGotoService:
    def get_goto_url(self, code: str) -> GotoResponse:
        pass
