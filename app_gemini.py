import os
import sys
from google import genai
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

cliente = genai.Client(api_key=api_key)

def ejecutar_consulta():
    print("Ejecutando consulta a Gemini...")

    try:
        respuesta = cliente.models.generate_content(
            model="gemini-3.5-flash",
            contents="Presentate como experto en ML y responde: Cuales son las mejores practicas para entrenar modelos de machine learning?"
        )
        print("Respuesta de Gemini:")
        print(respuesta.text)
    except Exception as e:
        print("Error al ejecutar la consulta:", e)

if __name__ == "__main__":
    ejecutar_consulta()
