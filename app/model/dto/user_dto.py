from typing import List
from pydantic import BaseModel, Field


class UserCreateRequest(BaseModel):
    username:str = Field(..., description="Username")
    email:str = Field(..., description="Email")
    password:str = Field(..., description="Password")
    
    