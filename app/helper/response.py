from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    code: int = Field(200, description="HTTP status code")
    msg: str = Field("success", description="HTTP status message")

    class Config:
        schema_extra = {
            "example": {
                "code": 200,
                "msg": "success",
            }
        }


class ErrorResponse(BaseResponse):
    error: str = Field(None, description="Error message")

    def __init__(self, error):
        super().__init__(code=500, msg="Internal Server Error")
        self.error = error

class SuccessResponse(BaseResponse):
    data: dict = Field(None, description="Response data")

    def __init__(self, data):
        super().__init__(code=200, msg="success")
        self.data = data