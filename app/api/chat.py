import traceback
from fastapi import APIRouter, Depends
from app.helper.response import SuccessResponse, ErrorResponse
from app.helper.depends import get_chat_service
from app.service.chat_service import ChatService
from app.helper.logger import logger


router = APIRouter()


@router.get("/")
async def chat(chat_service: ChatService = Depends(get_chat_service)):
    try:
        logger.info("***********************chat***********************")
        qnswer, history = chat_service.chat("劳动合同终止后，劳动者有权向用人单位要求劳动合同解除或者赔偿吗？", [])
        return SuccessResponse({"answer": qnswer, "history": history})
    except Exception as e:
        logger.error(traceback.print_exc())
        return ErrorResponse(str(e))

