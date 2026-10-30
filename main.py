from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# 1. Cargar y extraer texto del documento PDF
loader = PyPDFLoader("documento.pdf")
paginas = loader.load()
# Extraemos solo la primera página para esta prueba
texto_pagina = paginas[0].page_content 

# 2. Instanciar el modelo ligero
llm = OllamaLLM(model="llama3.2:1b")

# 3. Definir las instrucciones (Prompt)
plantilla = """
Eres un asistente experto en análisis de documentos. Lee el siguiente texto extraído de un PDF y redacta un resumen con los 3 puntos más importantes.

Texto del documento:
{texto}

Puntos clave:
"""
prompt = PromptTemplate.from_template(plantilla)

# 4. Construir la cadena LCEL y ejecutarla
cadena = prompt | llm
respuesta = cadena.invoke({"texto": texto_pagina})

print("--- Análisis del PDF ---")
print(respuesta)