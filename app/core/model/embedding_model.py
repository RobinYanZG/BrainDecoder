from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from app.core.device_management import device

class EmbeddingModel(HuggingFaceEmbeddings):
    def __init__(self):
        super().__init__(
            model_name='shibing624/text2vec-base-chinese', 
            model_kwargs={'device': device.get_embedding_device()}
        )