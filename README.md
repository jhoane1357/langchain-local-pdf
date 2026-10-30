# LangChain + Ollama - Resumen de PDF local

Este proyecto demuestra cómo usar LangChain y Ollama para cargar un archivo PDF local, extraer el texto de una página y generar un resumen con un modelo de lenguaje ejecutado localmente.

## Descripción

La aplicación hace lo siguiente:

- carga un archivo PDF desde el directorio del proyecto
- extrae el contenido de la primera página
- usa un modelo LLM local con Ollama
- crea un prompt para resumir los puntos clave del documento
- imprime el resultado en consola

## Tecnologías utilizadas

- Python
- LangChain
- LangChain Community
- LangChain Ollama
- Ollama
- PyPDF

## Estructura del proyecto

```text
LangChain_ollama/
├── .gitignore
├── .venv/
├── documento.pdf
├── main.py
├── README.md
└── .venv/
```

## Requisitos previos

1. Tener Python 3.10 o superior instalado.
2. Tener Ollama instalado y funcionando en tu equipo.
3. Descargar el modelo que vas a usar, por ejemplo:

```bash
ollama pull llama3.2:1b
```

4. Crear y activar un entorno virtual (opcional, pero recomendado).

## Instalación

Desde la raíz del proyecto:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install langchain langchain-community langchain-ollama pypdf
```

## Uso

1. Coloca tu archivo PDF dentro de la carpeta del proyecto con el nombre `documento.pdf`.
2. Ejecuta el script:

```bash
python main.py
```

3. La aplicación mostrará un resumen con los 3 puntos más importantes del PDF.

## Configuración importante

El proyecto usa esta línea para cargar el archivo PDF:

```python
loader = PyPDFLoader("documento.pdf")
```

Si tu archivo PDF tiene otro nombre, cambia el valor en `main.py`.

## Nota

Este ejemplo está pensado para trabajar con modelos locales de Ollama, lo que permite ejecutar IA sin depender de servicios externos.

## Autor

Jhoane
