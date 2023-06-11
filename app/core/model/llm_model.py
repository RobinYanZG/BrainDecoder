from transformers import AutoTokenizer, AutoModel


class LLMModel:
    model: object = None
    tokenizer: object = None
    
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int8", trust_remote_code=True)
        self.model = AutoModel.from_pretrained("THUDM/chatglm-6b-int8", trust_remote_code=True).half().cuda()

    def chat(self, prompt: str, history: list) -> tuple:
        return self.model.chat(self.tokenizer, prompt, history=history)