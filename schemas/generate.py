from typing import Any, List, Optional

from pydantic import BaseModel


class GenerateRequest(BaseModel):
    query: str = ""
    temperature: float = 0.0
    max_new_tokens: int = 500
    history: List[Any] = []
    system_prompt: Optional[str] = None


class GenerateResponse(BaseModel):
    result: str = ""
