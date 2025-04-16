from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.classify import classify_category
from typing import Dict, List, Any

router = APIRouter()

# 요청 스키마
class ClassifyRequest(BaseModel):
    todo: str

# 응답 스키마
class ClassifyResponse(BaseModel):
    category: str
    similarity: float
    isNew: bool
    embedding: List[float]

@router.post("/classify-category", response_model=ClassifyResponse)
def classify(req: ClassifyRequest):
    try:
        return classify_category(req.todo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
