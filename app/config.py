import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# Ollama 설정
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "mistral")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_GENERATE_ENDPOINT = f"{OLLAMA_BASE_URL}/api/generate"
