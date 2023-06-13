import traceback
from fastapi import APIRouter, Depends, Body
from app.helper.depends import get_chat_service, get_history_service
from app.helper.logger import logger
from app.helper.response import SuccessResponse, ErrorResponse
from app.model.dto.chat_dto import ChatRequest
from app.model.user import User
from app.service.chat_service import ChatService


router = APIRouter()

def get_vector_index():
    return 'LaborLaw'


@router.post("/")
async def chat(
    chat_service: ChatService = Depends(get_chat_service),
    history_service = Depends(get_history_service),
    query_obj: ChatRequest = Body(..., description="User Query"),
):
    try:
        historyMessage = []
        hasConversation = history_service.check_coversation_exists(query_obj.conversation_id, query_obj.user_id)
        if hasConversation:
            historyMessage = history_service.get_history(query_obj.conversation_id)
        
        logger.info(f"History message: {historyMessage}")
        
        vector_index = get_vector_index()
        logger.info(f"Vector Store: {vector_index}")
        
        answer, history = chat_service.chat(
            query=query_obj.query, 
            history=historyMessage,
            vector_index=vector_index
        )
        return SuccessResponse({"answer": answer, "history": history})
    except Exception as e:
        logger.error(traceback.print_exc())
        return ErrorResponse(str(e))

@router.get("/test")
async def test():
    users = User.select()
    return SuccessResponse({'users': [user.username for user in users]})