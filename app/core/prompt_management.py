from pydantic import BaseModel, Field
from typing import List, Tuple
from langchain.docstore.document import Document


PROMPT_TEMPLATE = """已知信息：
{context} 

根据上述已知信息，以专业律师的角度，用简洁和专业的来回答用户的问题。如果无法从中得到答案，请说 “根据已知信息无法回答该问题” 或 “没有提供足够的相关信息”，不允许在答案中添加编造成分，答案请使用中文。 问题是：{question}"""


class PromptManagement(BaseModel):
    template: str = Field(PROMPT_TEMPLATE, description="模板")
    
    def generate_prompt(
        self,
        related_docs: List[Tuple[Document, float]], 
        query: str,
    ) -> str:
        context = "\n".join([doc[0].page_content for doc in related_docs])
        prompt = self.template.replace("{question}", query).replace("{context}", context)
        return prompt
    