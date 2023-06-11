from app.core.model.embedding_model import EmbeddingModel
from app.core.model.llm_model import LLMModel
from app.core.prompt_management import PromptManagement
from app.core.vector_store_management import VectorStoreManagement


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
    
    def chat(self, query: str, history: list) -> tuple:
        self.vsMngr.load("LaborLaw", self.embedding)
        
        related_docs_with_score = self.vsMngr.similarity_search(query, k=10)
        prompt = self.prompt_mngr.generate_prompt(related_docs_with_score, query)
        
        response, history = self.llm_model.chat(prompt, history)
        return response, history
    
chat_management = ChatManagement()