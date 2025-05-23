import json
from app.config import SessionLocal
from sqlalchemy import text

def get_category_embeddings() -> dict:
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT name, embedding_json FROM category")).mappings()
        category_vectors = {}
        for row in result:
            name = row["name"]
            raw_json = row["embedding_json"]
            if not raw_json:
                continue
            vec = json.loads(raw_json)
            category_vectors[name] = vec
        return category_vectors
    finally:
        db.close()

        
def save_category_to_db(name: str, embedding: list):
    from app.config import SessionLocal
    import json
    from sqlalchemy import text

    db = SessionLocal()
    try:
        embedding_json = json.dumps(embedding.tolist())
        db.execute(
            text("INSERT IGNORE INTO category (name, embedding_json) VALUES (:name, :embedding)"),
            {"name": name, "embedding": embedding_json}
        )
        db.commit()
    finally:
        db.close()


