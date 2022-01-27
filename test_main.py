from typing import Dict
from fastapi import status
from fastapi.testclient import TestClient
from starlette.responses import Response
from controller.models.request.create_short_code import CreateShortCodeRequest
from main import app
from controller import short_code, goto
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
    id: str = 'testid'
    expected_response: Dict[str, str] = {
        'url': 'http://www.google.com', 'shortCode': 'ww', 'id': 'testid'}

    # ACT
    response: Response = test_client.get(f"/short-code/{id}")

    # ASSERT
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_search_short_code_by_url() -> None:
    # ARRANGE
    url: str = 'http://www.google.com'
    expected_response: Dict[str, str] = {'list': [
        {'url': 'http://www.google.com', 'shortCode': None, 'id': 'test1'}], 'count': 1}

    # ACT
    response: Response = test_client.get(f"/short-code?url={url}")

    # ASSERT
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_search_short_code_by_code() -> None:
    # ARRANGE
    code: str = 'foo'
    expected_response: Dict[str, str] = {'list': [
        {'url': None, 'shortCode': 'foo', 'id': 'test1'}], 'count': 1}

    # ACT
    response: Response = test_client.get(f"/short-code?code={code}")

    # ASSERT
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_create_short_code() -> None:
    # ARRANGE
    request: CreateShortCodeRequest = CreateShortCodeRequest(
        url='http:www.google.com')

    expected_response: Dict[str, str] = {
        'url': 'http://www.pacna.com/goto/blah'}

    # ACT
    response: Response = test_client.post('/short-code', json=request.dict())

    # ASSERT
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_get_goto_url() -> None:
    # ARRANGE
    short_code: str = '9x'
    expected_response: Dict[str, str] = {
        'url': 'http://www.google.com'
    }

    # ACT
    response: Response = test_client.get(f'/goto/{short_code}')

    # ASSERT
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response
