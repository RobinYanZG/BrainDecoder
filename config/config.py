import os
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # http server
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    
    # AI Model
    EMBEDDING_MODEL: str = "shibing624/text2vec-base-chinese"
    LLM_MODEL: str = "THUDM/chatglm-6b-int8"

    # database
    DB_HOST: str = Field('host', env='DB_HOST')
    DB_PORT: int = Field(5432, env='DB_PORT')
    DB_USER: str = Field('user', env='DB_USER')
    DB_PASSWORD: str = Field('pwd', env='DB_PASSWORD')
    DB_NAME: str = Field('db', env='DB_NAME')

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        

settings = Settings()