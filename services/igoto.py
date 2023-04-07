from typing import Protocol
from controllers.models.response.goto import GotoResponse


class IGotoService(Protocol):
    def get_goto_url(self, code: str) -> GotoResponse:
        ...
