from fastapi import APIRouter

from api.api_v1.endpoints import generate


api_router = APIRouter()
api_router.include_router(generate.router, prefix="/generate")


@api_router.get("/ping")
def ping():
    return {"message": "Success"}
