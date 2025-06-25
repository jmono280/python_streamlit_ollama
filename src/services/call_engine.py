from src.services.llm_service import LLMService

"""Calse para llamar el modelo"""


class Engine:
    def __init__(self):
        self.llm_service = LLMService()

    def run_engine(self, query_text: str) -> str:
        """Run model"""
        response = self.llm_service.generate_response(query_text, "context")
        return response
