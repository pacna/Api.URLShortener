from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.openapi.utils import get_openapi
from controllers.short_code import ShortCodecontrollers
from controllers.goto import Gotocontrollers

app: FastAPI = FastAPI()
app.include_router(ShortCodecontrollers().router)
app.include_router(Gotocontrollers().router)


@app.get("/", include_in_schema=False)
def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API.URLShortener",
        version="0.0.1",
        description="A URL shortener service",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
