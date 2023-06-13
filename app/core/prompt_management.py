from pydantic import BaseModel, Field
from typing import List, Tuple
from langchain.docstore.document import Document


PROMPT_TEMPLATE = """已知信息：
{context} 

根据上述已知信息，以专业律师的角度，用简洁和专业的来回答用户的问题。如果无法从中得到答案，请说 “根据已知信息无法回答该问题” 或 “没有提供足够的相关信息”，不允许在答案中添加编造成分，答案请使用中文。 问题是：{question}"""

PROMPT_TEMPLATE_WITHOUT_KS = "以专业律师的角度，用简洁和专业的来回答用户的问题。 问题是：{question}"


class PromptManagement(BaseModel):
    template: str = Field(PROMPT_TEMPLATE, description="模板")
    template_without_ks: str = Field(PROMPT_TEMPLATE_WITHOUT_KS, description="无知识库匹配的模板")
    
    def generate_prompt(
        self,
        related_docs: List[Document], 
        query: str,
    ) -> str:
        if len(related_docs) == 0:
            prompt = self.template_without_ks.replace("{question}", query)
            return prompt
        
        context = "\n".join([doc.page_content for doc in related_docs])
        prompt = self.template.replace("{question}", query).replace("{context}", context)
        return prompt
    