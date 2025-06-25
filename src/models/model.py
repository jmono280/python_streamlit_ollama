from langchain_ollama import OllamaLLM
import subprocess


"""Clase para gestionar los modelos disponibles en el sistema.

Attributes:
    models (list): Lista de nombres de modelos disponibles en ollama.

Methods:
    get_available_models(): Obtiene y actualiza la lista de modelos disponibles.
    display_models(): Muestra los modelos en un formato claro.
"""


class ModelManager:
    """Gestor de modelos para el sistema"""

    def __init__(self):
        """Inicializa el gestor de modelos con una lista vacía."""
        self.models = []

    def get_available_models(self) -> list:
        """Obtiene la lista de modelos disponibles en el sistema.

        Usa diferentes métodos según esté disponible:
          1. Comando de línea de comandos

        Returns:
            list: Lista de nombres de modelos disponibles
        """
        try:
            # Uso de línea de comandos
            cmd_output = subprocess.check_output(["ollama", "list"], text=True)
            # Extraer los nombres de modelo de la salida del comando
            self.models = [
                line.split()[0]
                for line in cmd_output.strip().split("\n")
                if "Available" not in line
            ]

            # Filtrar los nombres de modelo que no contienen "NAME", nombre de la columna
            filtered_models = [
                model for model in self.models if "NAME" not in model.upper()
            ]

            return filtered_models

        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            return f"Error al ejecutar comando: {str(e)}"

    def check_available_models(self) -> bool:
        # Filtrar modelos que contienen "NAME"
        filtered_models = [
            model for model in self.models if "NAME" not in model.upper()
        ]

        return len(filtered_models) > 0

    """Esta se debe activar en el main, permite 
        ver la salida de los modelos disponibles en Ollama por consola.
    """

    def display_models(self, flag: bool):
        """Muestra los modelos disponibles en un formato claro."""
        if flag:
            if not self.models:
                try:
                    # Intentamos actualizar la lista si está vacía
                    print("Actualizando lista de modelos...")
                    self.get_available_models()
                except Exception as e:
                    print(f"Error al obtener modelos: {str(e)}")

            if not self.models:
                print("No se pudieron encontrar modelos disponibles.")
                return

            print("\n🔍 Modelos de IA disponibles en su sistema:")
            print("----------------------------------------")

            # Ordenamos alfabéticamente y mostramos con un formato claro
            sorted_models = sorted(self.models)

            filtered_models = [
                model for model in sorted_models if "NAME" not in model.upper()
            ]

            for idx, model in enumerate(filtered_models, 1):
                print(f"{idx}. {model}")

            print("\nTotal de modelos disponibles:", len(filtered_models))


# Ejemplo de uso: si se quiere ejecuar solo este modelo por consola para ver si ollama contiene modelos descagadod
# python3 src/models/model.py
if __name__ == "__main__":
    manager = ModelManager()
    models_list = manager.get_available_models()
    manager.display_models(True)
    print(manager.check_available_models())

    if len(models_list) > 0:
        print("\n¡Modelos encontrados! Puede usarlos en su aplicación.")
        print(models_list)
