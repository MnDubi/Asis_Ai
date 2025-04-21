import requests
from app.config import OLLAMA_GENERATE_ENDPOINT, OLLAMA_MODEL_NAME

def generate_category_name(todo: str) -> str:
    prompt = f"""
    "{todo}" 라는 할 일에 어울리는 상위 카테고리를 **한 단어**로 추천해줘.
    절대 영어 말고, 한국어로만 추천해줘. 예: 공부, 운동, 쇼핑, 청소, 계획
    답변은 카테고리명 하나만 출력해. '기타'는 절대 추천하지 마.
    """

    print("[🟡 요청 전송]")
    print(f"모델: {OLLAMA_MODEL_NAME}")
    print(f"프롬프트: {prompt.strip()}")

    try:
        response = requests.post(OLLAMA_GENERATE_ENDPOINT, json={
            "model": OLLAMA_MODEL_NAME,
            "prompt": prompt,
            "stream": False
        })

        print("[🟢 응답 도착]")
        print("Status:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            print("응답 내용:", data)

            if "response" in data:
                raw = data["response"]
                cleaned = raw.strip().strip('"')  # 따옴표 제거
                return cleaned.split("\n")[0]
            elif "message" in data:
                return data["message"].strip().split("\n")[0]
            else:
                return "기타"
        else:
            print("비정상 응답 → 기타 반환")
            return "기타"

    except Exception as e:
        print("⚠️ 예외 발생:", e)
        return "기타"
