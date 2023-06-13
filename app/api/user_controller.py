import traceback
from fastapi import APIRouter, Depends, Body
from app.helper.depends import get_user_service
from app.helper.logger import logger
from app.helper.response import SuccessResponse, ErrorResponse
from app.model.dto.user_dto import UserCreateRequest
from app.service.user_service import UserService


router = APIRouter()


@router.post("/create")
async def create(
    user_service: UserService = Depends(get_user_service),
    user_info: UserCreateRequest = Body(..., description="User param"),
):
    try:
        result = user_service.create(
            user_info.username, user_info.password, user_info.email
        )
        return SuccessResponse(result)
    except Exception as e:
        logger.error(traceback.print_exc())
        return ErrorResponse(str(e))
