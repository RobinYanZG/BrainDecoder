from app.core.model.embedding_model import EmbeddingModel
from app.core.model.llm_model import LLMModel
from app.core.prompt_management import PromptManagement
from app.core.vector_store_management import VectorStoreManagement
from app.core.torch_management import torchMngr
from app.helper.logger import logger


class ChatManagement: 
    llm_model: LLMModel
    embedding: EmbeddingModel
    prompt_mngr: PromptManagement
    vsMngr: VectorStoreManagement
    
    def __init__(self):
        self.llm_model = LLMModel()
        self.embedding = EmbeddingModel()
        self.prompt_mngr = PromptManagement()
        self.vsMngr = VectorStoreManagement()
    
    def chat_with_store(self, query: str, history: list, vector_index: str = "LaborLaw") -> tuple:
        logger.info(f"Chatting with query: {query}")
        logger.info("loading vector store")
        self.vsMngr.load(vector_index, self.embedding)
        
        logger.info("searching for similar documents")
        related_docs = self.vsMngr.similarity_search_under_score(query, 500) # score越接近0越好，太大不相关
        print(related_docs)
        
        torchMngr.gc()
        
        logger.info("generating prompt")
        prompt = self.prompt_mngr.generate_prompt(related_docs, query)
        logger.info(f"prompt: {prompt}")
        
        logger.info("chatting with llm model")
        response, history = self.llm_model.chat(prompt, history)
        logger.info(f"answer: {response}")
        torchMngr.gc()
        return response, history
    
chat_management = ChatManagement()