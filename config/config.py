import os
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    BASE_PATH: str = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000


settings = Settings()