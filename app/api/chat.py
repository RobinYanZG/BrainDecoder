import traceback
from fastapi import APIRouter, Depends, Body
from app.helper.depends import get_chat_service
from app.helper.logger import logger
from app.helper.response import SuccessResponse, ErrorResponse
from app.model.dto.chat import ChatRequest
from app.service.chat_service import ChatService


router = APIRouter()


@router.post("/")
async def chat(
    chat_service: ChatService = Depends(get_chat_service),
    query_obj: ChatRequest = Body(..., description="User Query"),
):
    try:
        logger.info("***********************chat***********************")
        answer, history = chat_service.chat(
            query=query_obj.query, 
            history=query_obj.history,
            vector_index=query_obj.vector_index
        )
        return SuccessResponse({"answer": answer, "history": history})
    except Exception as e:
        logger.error(traceback.print_exc())
        return ErrorResponse(str(e))

