# Agente de Atención Virtual - Mercado Central 24h

Este proyecto es un chatbot interactivo para terminal desarrollado en Python. Utiliza la API de Google Gemini para procesar documentos PDF (reglamentos, políticas y procedimientos) y responder preguntas de los usuarios basándose exclusivamente en la información proporcionada.

---

## 🚀 Características

* **Extracción de PDF:** Procesa reglamentos y documentación en formato PDF mediante `pypdf`.
* **Respuestas basadas en contexto:** Configurado con instrucciones de sistema para no inventar información fuera del documento.
* **Modelo Gemini:** Integración con la API oficial de Google Gemini (`gemini-flash-latest`).
* **Seguridad:** Gestión de credenciales mediante variables de entorno con `python-dotenv`.

---

## 📁 Estructura del Proyecto

```text
challenge-alura-agente/
│
├── agente.py                  # Código principal del chatbot
├── requirements.txt           # Dependencias del proyecto
├── .gitignore                 # Archivos excluidos de Git (.env, cache, etc.)
├── README.md                  # Documentación del proyecto
├── inventario_de_supermercado_latam.xlsx # Datos de inventario
│
└── 📄 Documentos PDF de Referencia
    ├── Reglamento.pdf
    ├── Politica de Atención al Cliente y Devoluciones.pdf
    ├── Manual de Proveedores y Política de Compras.pdf
    └── Preguntas Frecuentes (FAQ).pdf
```

## 🛠️ Requisitos e Instalación
1. Clona este repositorio:
```bash
git clone https://github.com/Uzielzz/challenge-alura-agente.git
cd challenge-alura-agente
```
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```
3. Configura tu clave de API:
Crea un archivo .env en la raíz del proyecto y agrega tu API Key de Gemini:
```bash
GEMINI_API_KEY="TU_API_KEY_AQUI"
```
## 💡 Uso del Agente
​Para iniciar el chatbot interactivo en la terminal, ejecuta:
```bash
python agente.py
```
Ejemplo de interacción:
```bash
INICIANDO SCRIPT
Cargando el documento: Reglamento.pdf...
¡Documento cargado y procesado exitosamente!

CHATBOT DE TERMINAL INICIADO
Escribe tu pregunta sobre el documento. Escribe 'salir' para terminar.

Tú: ¿Cuál es la política de devoluciones?
Agente: [Respuesta basada estrictamente en la documentación]
```
## ⚙️ Tecnologías Utilizadas
​Lenguaje: Python 3.x
​IA: Google Gemini API (google-genai)
​Librerías: pypdf, python-dotenv


