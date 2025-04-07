from app.services.embedding import get_embedding, cosine_similarity
from app.utils.gpt_local import generate_category_name

def classify_category(todo: str, category_vectors: dict) -> dict:
    """
    투두 문장을 기반으로 카테고리를 분류하거나 새로 생성한다.
    """
    todo_vec = get_embedding(todo)

    # Step 1: 기존 카테고리들과 cosine similarity 계산
    best_match = None
    max_sim = 0.0
    for name, vec in category_vectors.items():
        sim = cosine_similarity(todo_vec, vec)
        if sim > max_sim:
            max_sim = sim
            best_match = name

    # Step 2: 유사한 카테고리 있으면 바로 반환
    if max_sim >= 0.7:
        return {
            "category": best_match,
            "similarity": round(max_sim, 4),
            "isNew": False,
            "embedding": todo_vec.tolist()
        }

    # Step 3: GPT로 새 카테고리 생성
    new_category = generate_category_name(todo)

    return {
        "category": new_category,
        "similarity": round(max_sim, 4),
        "isNew": True,
        "embedding": todo_vec.tolist()
    }
