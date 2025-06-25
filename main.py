import streamlit as st
from src.models.model import ModelManager
from src.services.llm_service import LLMService
from src.ui.view import View, QueryForm, ResultsDisplay, QueryChatForm
import time


def main():

    # Crear una instancia de ModelManager
    model_manager = ModelManager()

    # Obtener los modelos disponibles
    model_manager.get_available_models()

    # True para ver en consola los modelos disponibles
    model_manager.display_models(False)

    view = View(model_manager)

    # # Mostrar la interfaz
    view.show_model_selection()

    # Verificar si se han cargado los modelos
    if model_manager.check_available_models():
        st.write("✅ Modelo seleccionado: ", view._current_model_name)
    else:
        st.error("❌ No hay modelos disponibles")

    run_engine = LLMService(model_name=view._current_model_name)

    query = QueryChatForm()

    with st.spinner("Generando respuesta...", show_time=True):
        if query:
            start_time = time.time()
            response = run_engine.generate_response(query.query_text)
            is_building = True  # Indica que estamos en un proceso
            results_display = ResultsDisplay()
            st.write("✅ pregunta: ", query.query_text.text)
            results_display.display(response, is_building=is_building)
            elapsed_time = time.time() - start_time
            st.write(f"respondido en {elapsed_time} segundos")


if __name__ == "__main__":
    main()
