import torch

class TorchManagement:
    embedding_device: str
    llm_device: str
    is_cuda: bool
    
    def __init__(self):
        self.embedding_device = "cpu"
        self.is_cuda = torch.cuda.is_available()
        self.llm_device = "cuda" if self.is_cuda else "cpu"
    
    def get_lllm_device(self):
        return self.llm_device
    
    def get_embedding_device(self):
        return self.embedding_device
    
    def gc(self):
        if self.is_cuda:
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
        

torchMngr = TorchManagement()
