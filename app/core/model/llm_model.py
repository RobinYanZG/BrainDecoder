from transformers import AutoTokenizer, AutoModel, PreTrainedTokenizer, PreTrainedTokenizerFast, PreTrainedModel
from app.core.torch_management import torchMngr
from config.config import settings


class LLMModel:
    model: PreTrainedModel
    tokenizer: PreTrainedTokenizer | PreTrainedTokenizerFast
    llm_device: str
    
    def __init__(self):
        self.llm_device = torchMngr.get_lllm_device().lower()
        self.tokenizer = AutoTokenizer.from_pretrained(settings.LLM_MODEL, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(settings.LLM_MODEL, trust_remote_code=True)
        if self.llm_device.startswith("cuda"):
            self.model = self.model.half().cuda()
        else:
            self.model = self.model.float().to(self.llm_device)

    def chat(self, prompt: str, history: list) -> tuple:
        return self.model.chat(self.tokenizer, prompt, history=history)