import torch

class DeviceManagement:
    embedding_device: str
    llm_device: str
    
    def __init__(self):
        self.embedding_device = "cpu"
        self.llm_device = "cuda" if torch.cuda.is_available() else "cpu"
    
    def get_lllm_device(self):
        return self.llm_device
    
    def get_embedding_device(self):
        return self.embedding_device
    
device = DeviceManagement()