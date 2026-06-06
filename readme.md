# Gemini API - Conexión básica con Python

## Descripción

Este proyecto demuestra cómo conectarse a la **API de Gemini de Google** desde Python para generar respuestas de inteligencia artificial. El script envía una pregunta sobre Machine Learning al modelo `gemini-3.5-flash` y muestra la respuesta en la terminal.

Es un punto de partida ideal para cualquier persona que quiera comenzar a integrar modelos de lenguaje de Google en sus proyectos Python.

---

## Tecnologías utilizadas

- **Python 3.x**
- **google-genai** — SDK oficial de Google para la API de Gemini
- **python-dotenv** — para manejar variables de entorno de forma segura

---

## Estructura del proyecto

```
gemini-api/
├── app_gemini.py       # Script principal
├── .env                # Tu API key (debes crearlo tú, no está en el repo)
├── .gitignore          # Archivos ignorados por Git
├── requeriments.txt    # Dependencias
├── README.md           # Este archivo
└── images/
    └── evidencia.png   # Captura de la ejecución
```

---

## Paso 1 — Obtener una API key de Google

1. Ve a [https://aistudio.google.com](https://aistudio.google.com)
2. Inicia sesión con tu cuenta de Google
3. Haz clic en **"Get API key"** → **"Create API key"**
4. Copia la key generada, la necesitarás en el Paso 4

---

## Paso 2 — Clonar el repositorio

Abre una terminal y ejecuta:

```bash
git clone https://github.com/arleyrativa6/gemini-api-demo.git
cd gemini-api-demo
```

---

## Paso 3 — Instalar las dependencias

```bash
pip install google-genai python-dotenv
```

---

## Paso 4 — Configurar la API key

Crea un archivo llamado `.env` en la raíz del proyecto y pega lo siguiente:

```
GEMINI_API_KEY=aquí_va_tu_api_key
```

> **Nunca compartas este archivo.** El `.gitignore` ya está configurado para que Git lo ignore y no se suba accidentalmente a GitHub.

---

## Paso 5 — Ejecutar el script

```bash
python app_gemini.py
```

Si todo está bien configurado, verás en la terminal una respuesta generada por Gemini sobre las mejores prácticas de Machine Learning.

---

## Cómo funciona el código

```python
# Carga la API key desde el archivo .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Inicializa el cliente de Gemini con la key
cliente = genai.Client(api_key=api_key)

# Envía la consulta al modelo y obtiene la respuesta
respuesta = cliente.models.generate_content(
    model="gemini-3.5-flash",
    contents="tu pregunta aquí"
)

# Imprime el texto de la respuesta
print(respuesta.text)
```

---

## Posibles errores

| Error | Causa | Solución |
|-------|-------|----------|
| `RESOURCE_EXHAUSTED` | Cuota de la API agotada | Espera unos minutos o revisa tu plan en Google AI Studio |
| `NOT_FOUND` | El modelo no existe o no está disponible | Cambia el modelo por otro de la lista disponible |
| `No module named 'google'` | Dependencias no instaladas | Ejecuta `pip install google-genai python-dotenv` |
| La API key no carga | El archivo `.env` no existe o tiene un error | Verifica que el archivo `.env` esté en la raíz del proyecto |

---

## Evidencia de ejecución

![Ejecución del script](images/evidencia.png)
