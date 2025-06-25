import streamlit as st
from src.models.model import ModelManager
from src.models.query import Query
from src.utils.print_in_color import print_in_color
from typing import Optional  # Asegúrate de que este módulo esté importado


class View:
    """Clase que maneja la interfaz de usuario y maneja el modelo seleccionado"""

    def __init__(self, model_manager: ModelManager) -> list:
        self._model_manager = model_manager
        self._current_model_name: str = None

    def show_model_selection(self) -> None:
        """Muestra la lista de modelos disponibles"""
        st.set_page_config(
            page_title="LLaMA Interfaz", layout="centered", page_icon="🦙"
        )

        with st.form("llama interaction") as form:
            with st.sidebar.expander("Configuración", expanded=True):
                # Filtrar los nombres de modelo que no contienen "NAME"
                filtered_models = [
                    model
                    for model in self._model_manager.models
                    if "NAME" not in model.upper()
                ]

                selected_model = st.selectbox(
                    "Selecione un modelo local (Ollama):",
                    options=filtered_models,
                    key="selected_model",
                )

                st.write("Parámetros del modelo:")
                params = st.text_input("Temperatura:", value="0.8")

        # Variable para el estado del modelo seleccionado
        if selected_model:
            self._current_model_name = selected_model


def QueryChatForm():
    """Muestra el formulario de consulta"""
    # Crea un input chat
    query_text = st.chat_input(
        "Ingrese su pregunta:",
        accept_file=True,
        file_type=["pdf", "docx", "txt"],
        key="query_input",
    )

    if query_text:
        query = Query(query_text=query_text)
        return query


"""Calse para manejar el tiempo de ejecución del modelo y mostrar la respuesta en pantalla"""


class ResultsDisplay:
    def __init__(self):
        self.is_building: bool = False

    def display(self, response: str, is_building: Optional[bool] = None):
        """Muestra la respuesta o un mensaje de procesando"""
        if is_building is not None:
            self.is_building = is_building
        else:
            self.is_building = False

        st.title("Respuesta:")
        st.write(response)
