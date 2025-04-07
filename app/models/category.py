import openai
import os
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_category_name(todo: str) -> str:
    """
    OpenAI GPT를 사용하여 todo 문장에 맞는 상위 카테고리명을 한 단어로 생성
    """
    prompt = f"""
    "{todo}" 라는 할 일에 어울리는 상위 카테고리를 **한 단어(2~4글자)**로 정해줘.
    절대 영어 말고, 한국어로만 추천해줘. 예: 공부, 운동, 쇼핑, 청소, 계획
    답변은 카테고리명 하나만 출력해.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=10,
        temperature=0.5
    )

    category_name = response.choices[0].message["content"].strip()
    return category_name
