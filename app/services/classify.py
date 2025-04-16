from app.services.embedding import get_embedding, cosine_similarity
from app.utils.gpt_local import generate_category_name
from app.services.embedding import get_embedding, cosine_similarity
from app.utils.gpt_local import generate_category_name
from app.db.category_db import get_category_embeddings 
from app.db.category_db import save_category_to_db

def classify_category(todo: str) -> dict:
    category_vectors = get_category_embeddings() 
    todo_vec = get_embedding(todo)

    best_match = None
    max_sim = 0.0
    for name, vec in category_vectors.items():
        sim = cosine_similarity(todo_vec, vec)
        if sim > max_sim:
            max_sim = sim
            best_match = name

    if max_sim >= 0.7:
        return {
            "category": best_match,
            "similarity": round(max_sim, 4),
            "isNew": False,
            "embedding": todo_vec.tolist()
        }

    new_category = generate_category_name(todo)
    new_vec = get_embedding(new_category)

    # 자동 저장
    save_category_to_db(new_category, new_vec)

    return {
        "category": new_category,
        "similarity": round(max_sim, 4),
        "isNew": True,
        "embedding": todo_vec.tolist()
    }