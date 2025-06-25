from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate  # type: ignore

"""Calse encargada de generar la consulta y obtener la respuesta del modelo"""


class LLMService:
    def __init__(self, model_name=""):
        self.model = OllamaLLM(model=model_name)
        template = """You are an exeprt in answering questions about anithyng about computer programation,
                    like python, java, javascript y backend
                    Here is the context in case you need it: {context}
                    Here is the question to answer: {question}"""

        prompt_template = ChatPromptTemplate.from_template(template)
        self.prompt = prompt_template
        self.chain = self.prompt | self.model

    def answer_question(self, question, context: str = ""):

        return self.chain.invoke({"context": context, "question": question})

    def generate_response(self, query_text: str, context: str = "") -> str:
        prompt = {"context": context, "question": query_text}

        response = self.answer_question(prompt)
        return response
