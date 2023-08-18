from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.openapi.utils import get_openapi
from uvicorn import Config, Server
from controllers import short_code, goto

app: FastAPI = FastAPI()
app.include_router(short_code.router)
app.include_router(goto.router)


@app.get("/", include_in_schema=False)
def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API.URLShortener",
        version="0.0.1",
        description="A Python-based service that provides a simple way to shorten long URLs, making them easier to share and remember.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    server = Server(Config("main:app", port=8000, log_level="info"))
    server.run()
