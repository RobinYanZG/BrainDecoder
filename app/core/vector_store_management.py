from langchain.vectorstores import FAISS
import os

from app.core.model.embedding_model import EmbeddingModel


vector_store_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "vector_store")


class VectorStoreManagement: 
    vector_store: FAISS
    
    def load(self, index_key: str, embedding: EmbeddingModel) -> object:
        key = os.path.join(vector_store_path, index_key)
        print(key)
        self.vector_store = FAISS.load_local(key, embedding)
        
    def similarity_search(self, query: str, k: int) -> list:
        return self.vector_store.similarity_search_with_score(query, k)