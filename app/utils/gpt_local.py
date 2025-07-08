import requests
from app.config import OLLAMA_GENERATE_ENDPOINT, OLLAMA_MODEL_NAME
import re

def generate_category_name(todo: str) -> str:
    prompt = f"""
    "{todo}" 이 활동을 대표하는 상위 카테고리를 한국어로 한 단어로만 말해주세요.
    조건: 특수문자 없이, 의미 있는 상위 카테고리 단어만, "기타"는 금지.
    출력: 한 단어 (예: 운동, 여행, 공부, 청소, 계획, 쇼핑, 독서, 요리, 정리, 회의)
    """

    print("[🟡 요청 전송]")
    print(f"모델: {OLLAMA_MODEL_NAME}")
    # print(f"프롬프트: {prompt.strip()}")

    try:
        response = requests.post(OLLAMA_GENERATE_ENDPOINT, json={
            "model": OLLAMA_MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "max_tokens": 10,  # 출력 길이 제한
            "temperature": 0.5  # 생성 텍스트의 다양성 조정
        })

        print("[🟢 응답 도착]")
        # print("Status:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            

            if "response" in data:
                raw = data["response"]
                cleaned = raw.strip().splitlines()[0]  # 첫 줄만 가져오기
                cleaned = cleaned.strip().strip('"')  # 따옴표 제거
                cleaned = re.sub(r"[^\uAC00-\uD7A3]", "", cleaned)  # 한글만 남기기
                print("응답 내용:", cleaned)
                return cleaned

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
