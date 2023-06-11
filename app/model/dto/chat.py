from typing import List
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    query: str = Field("你好", description="User Query")
    history: List[List[str]] = Field([], description="Chat History")
    