from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.classify import classify_category
from typing import Dict, List, Any
import traceback

from app.services.classify import classify_category
from app.services.embedding import get_embedding
from app.db.category_db import save_category_to_db

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
    
class AddCategoryRequest(BaseModel):
    name: str


@router.post("/classify-category", response_model=ClassifyResponse)
def classify(req: ClassifyRequest):
    print(f"[🔥 classify 요청] todo = {req.todo}")
    try:
        return classify_category(req.todo)
    except Exception as e:
        print("[❌ 예외 발생]")
        traceback.print_exc()  # ← 에러 스택 출력
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/add-category")
def add_category(req: AddCategoryRequest):
    try:
        embedding = get_embedding(req.name)
        save_category_to_db(req.name, embedding)
        return {"message": f"카테고리 '{req.name}' 이(가) 성공적으로 추가되었습니다."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))