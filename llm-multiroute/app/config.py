import os


class Settings:
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", "8080"))
    APP_NAME: str = os.getenv("APP_NAME", "llm-multiroute")
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL","http://localhost:1234/v1")
    OLLAMA_TEMPERATURE: float = float(os.getenv("OLLAMA_TEMPERATURE", "0.7"))
    OLLAMA_API_KEY: str = os.getenv("OLLAMA_API_KEY", "lm-studio")

    # Per-route model assignments (must be available on Ollama cloud)
    OLLAMA_MODEL_CLASSIFY: str = os.getenv("OLLAMA_MODEL_CLASSIFY", "google/gemma-3n-e2b")
    OLLAMA_MODEL_SENTIMENT: str = os.getenv("OLLAMA_MODEL_SENTIMENT", "liquid/lfm2-1.2b")
    OLLAMA_MODEL_SUMMARIZE: str = os.getenv("OLLAMA_MODEL_SUMMARIZE", "mistralai/ministral-3-3b-reasoning")
    OLLAMA_MODEL_INTENT: str = os.getenv("OLLAMA_MODEL_INTENT", "google/gemma-3n-e2b")


settings = Settings()
