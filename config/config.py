import os
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    
    EMBEDDING_MODEL: str = "shibing624/text2vec-base-chinese"
    LLM_MODEL: str = "THUDM/chatglm-6b-int8"


settings = Settings()