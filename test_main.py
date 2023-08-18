from fastapi import status
from fastapi.testclient import TestClient
from starlette.responses import Response
from controllers.models.request.create_short_code import CreateShortCodeRequest
from main import app
from controllers import short_code, goto
from mocks.goto import TestGotoService
from mocks.short_code import TestShortService


short_code.service = TestShortService()
goto.service = TestGotoService()
test_client: TestClient = TestClient(app)


def test_get_root() -> None:
    # ACT
    response: Response = test_client.get("/")

    # ASSERT
    assert response.status_code == status.HTTP_200_OK


def test_get_short_code_by_id() -> None:
    # ARRANGE
    id: str = 'ww'
    expected_response: dict[str, str] = {
        'url': 'http://www.google.com', 'id': id}

    # ACT
    response: Response = test_client.get(f"/short-code/{id}")

    # ASSERT
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_search_short_code_by_url() -> None:
    # ARRANGE
    url: str = 'http://www.google.com'
    expected_response: dict[str, str] = {'list': [
        {'url': url, 'id': None}], 'count': 1}

    # ACT
    response: Response = test_client.get(f"/short-code?url={url}")

    # ASSERT
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_search_short_code_by_code() -> None:
    # ARRANGE
    code: str = 'foo'
    expected_response: dict[str, str] = {'list': [
        {'url': None, 'id': code}], 'count': 1}

    # ACT
    response: Response = test_client.get(f"/short-code?code={code}")

    # ASSERT
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_create_short_code() -> None:
    # ARRANGE
    request: CreateShortCodeRequest = CreateShortCodeRequest(
        url='http:www.google.com')

    expected_response: dict[str, str] = {
        'url': 'http://www.pacna.com/goto/blah'}

    # ACT
    response: Response = test_client.post('/short-code', json=request.model_dump())

    # ASSERT
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_get_goto_url() -> None:
    # ARRANGE
    short_code: str = '9x'
    expected_response: dict[str, str] = {
        'url': 'http://www.google.com'
    }

    # ACT
    response: Response = test_client.get(f'/goto/{short_code}')

    # ASSERT
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response
