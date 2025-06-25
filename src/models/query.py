"""Modelo para representar una consulta."""


class Query:
    def __init__(self, query_text: str, context: str = ""):
        self.query_text = query_text
        self.context = context  # For RAG context
