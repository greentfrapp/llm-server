from fastapi import APIRouter

import schemas
from utils.llm import generate


router = APIRouter()


@router.post("/generate", response_model=schemas.GenerateResponse, status_code=200)
def generate_post(payload: schemas.GenerateRequest):
    result = generate(
        query=payload.query,
        temperature=payload.temperature,
        max_new_tokens=payload.max_new_tokens,
        history=payload.history,
        system_prompt=payload.system_prompt
    )
    return {
        "result": result
    }
