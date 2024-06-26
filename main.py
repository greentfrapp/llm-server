from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api_v1.api import api_router as api_router_v1
from core.config import settings

app = FastAPI(
    openapi_url=None, docs_url=None, redoc_url=None,
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router_v1, prefix=settings.API_V1_STR)


@app.get("/ping")
def ping():
    return {"messsage": "Success"}
