from sentence_transformers import SentenceTransformer, util
import numpy as np

# 사전 훈련된 한국어 문장 임베딩 모델 (KoSimCSE or KLUE)
# 최초 로딩 시 다소 시간이 걸림
model = SentenceTransformer("jhgan/ko-sbert-sts")

def get_embedding(text: str) -> np.ndarray:
    """
    주어진 문장을 임베딩 벡터로 변환
    """
    return model.encode(text)

def cosine_similarity(vec1: list, vec2: list) -> float:
    """
    두 벡터 간 cosine similarity 계산
    """
    return float(util.cos_sim(vec1, vec2)[0][0])
