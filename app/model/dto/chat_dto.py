from typing import List
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    query: str = Field("你好", description="User Query")
    user_id: str = Field(..., description="User Id")
    conversation_id: str = Field(..., description="Conversation Id")
    
    