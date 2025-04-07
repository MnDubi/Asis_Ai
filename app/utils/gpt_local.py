import requests
from app.config import OLLAMA_GENERATE_ENDPOINT, OLLAMA_MODEL_NAME

def generate_category_name(todo: str) -> str:
    prompt = f"""
    다음 할 일에 어울리는 상위 카테고리를 한 단어로 추천해줘.
    할 일: "{todo}"
    예: 공부, 운동, 일정, 쇼핑 등
    카테고리명 하나만 출력해줘.
    """

    response = requests.post(OLLAMA_GENERATE_ENDPOINT, json={
        "model": OLLAMA_MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        return response.json().get("response", "").strip().split("\n")[0]
    else:
        return "기타"
