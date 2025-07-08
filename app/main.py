from fastapi import FastAPI
from app.router import api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="WPSCP Category Classifier API",
    description="투두리스트 자동 카테고리 분류 API",
    version="1.1.0"
)

# CORS 허용 (Spring 연동 대비)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 시 도메인 제한 권장
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(api.router)
