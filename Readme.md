# Python + Ollama + Streamlit -> Interactuar con modelos de IA locales

Si estás buscando una solución para interactuar directamente con modelos de IA locales con Ollama, Te voy a mostrar una forma facil y eficaz de dar los primeros pasos para tu proyecto.

**Objetivo del Proyecto:**

Una aplicación Streamlit que permite a los usuarios interactuar con modelos de IA locales atendidos por Ollama, con una base construida para el futuro entrenamiento RAG (Recuperación-Generación Aumentada).

**1. Estructura del Proyecto:**

```
local_ollama_streamlit/
├── src/
│   ├── models/                 # Directory for model-specific code
│   │   ├── models.py           # Class to handle model-specific logic
│   │   └── query.py            # Class to handle Ollama interactions
│   ├── services/               # Directory for model-specific code
│   │   ├── call_enginer.py     # Class to handle model-specific logic
│   │   └── llm_service.py      # Class to handle Ollama interactions
│   ├── ui/                     # Directory for model-specific code
│   │   └── view.py             # Class to handle Ollama interactions
│   └── utils/                  # Utility functions
│   │   └── print_in_color.py   # Class to handle Ollama interactions
│   ├── .env                    # Environment variables
│   └── config.py               # Environment variables initialization
├── main.py                     # Main Streamlit application logic
├── README.md                   # Project description and setup instructions
└── requirements.txt            # Python dependencies
```

**2. Explicación:**

- **langchain:** Framework para construir aplicaciones basadas en IA.
- **streamlit:** Para crear la interfaz de la aplicación.
- **ollama:** Para obtener los modeles de AI de forma local.
- **python 3.9+:** Para ejecutar el proyecto.

**3. Requerimientos:**

```markdown
- Python 3.9+
- Ollama installed and a model downloaded (ollama pull llama3.2)
```

## Setup

1.  Clona el repositorio: `git clone <repository_url>`
2.  Ingresa por linea de comandos dentro del repositorio..
3.  Install dependencies: `pip install -r requirements.txt`

## Futura actualizacion

- Implementar Autenticación de usuarios.
- Implementación de chat con historial de conversación para el modelo.
- Implementacion de RAG. con chroma y postgressql.
