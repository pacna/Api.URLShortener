from fastapi import status
from fastapi.testclient import TestClient
from starlette.responses import Response
from main import app

test_client: TestClient = TestClient(app)


def test_root():
    response: Response = test_client.get("/")
    assert response.status_code == status.HTTP_200_OK
