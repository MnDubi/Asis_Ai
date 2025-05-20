# 파일명: app/tools/reset_categories.py

from app.config import SessionLocal
from app.services.embedding import get_embedding
from app.db.category_db import save_category_to_db
from sqlalchemy import text

# 1. 기존 카테고리 전체 삭제
def delete_all_categories():
    db = SessionLocal()
    try:
        db.execute(text("DELETE FROM category"))
        db.commit()
        print("🧹 기존 카테고리 전체 삭제 완료")
    finally:
        db.close()

# 2. 내가 정의한 새 카테고리 목록
new_categories = [
    "운동", "공부", "미술", "창작", "개발", "요리", "여행",
    "청소", "계획", "독서", "쇼핑", "회의", "과제", "헬스",
    "취업", "청소", "연애", "행사", "학습", "교육", "행사"
]

# 3. 문장형 임베딩 생성 후 저장
def recreate_categories():
    for name in new_categories:
        sentence = f"{name} 관련 활동입니다."
        vec = get_embedding(sentence)
        save_category_to_db(name, vec)
        print(f"[✅ 생성됨] {name}")

# 4. 실행 함수
def reset_categories():
    delete_all_categories()
    recreate_categories()
    print("✅ 새 카테고리 재구성 완료")

# CLI 실행 가능
if __name__ == "__main__":
    reset_categories()
