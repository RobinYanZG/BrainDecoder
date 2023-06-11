import os
from pydantic import BaseSettings, Field


class Path(BaseSettings):
    BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    VECTOR_STORE_PATH: str = os.path.join(BASE_PATH, "vector_store")

path = Path()