import os
import streamlit as st
from google import genai
from pypdf import PdfReader

# Configuración de la página web
st.set_page_config(page_title="Asistente Mercado Central 24h", page_icon="🤖")
st.title("🤖 Asistente Virtual - Mercado Central 24h")

# 1. Configurar la API Key de Gemini desde los Secrets de Streamlit
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ No se encontró la API Key. Configura GEMINI_API_KEY en los Secrets de Streamlit.")
    st.stop()

client = genai.Client(api_key=api_key)

# 2. Búsqueda automática del archivo PDF de FAQ
@st.cache_data
def cargar_documento_faq():
    archivos = os.listdir('.')
    # Busca un archivo que sea .pdf y contenga "FAQ" o "Preguntas" en su nombre
    pdf_faq = next((f for f in archivos if f.endswith('.pdf') and ("FAQ" in f or "Preguntas" in f)), None)
    
    if not pdf_faq:
        # Si no encuentra por FAQ, toma el primer PDF disponible
        pdf_faq = next((f for f in archivos if f.endswith('.pdf')), None)
        
    if not pdf_faq:
        return None, "No se encontró ningún archivo PDF en la carpeta."

    try:
        reader = PdfReader(pdf_faq)
        texto = ""
        for page in reader.pages:
            extraido = page.extract_text()
            if extraido:
                texto += extraido + "\n"
        return texto, pdf_faq
    except Exception as e:
        return None, str(e)

document_text, nombre_pdf = cargar_documento_faq()

if not document_text:
    st.error(f"❌ Error al cargar el documento: {nombre_pdf}")
    st.stop()
else:
    st.caption(f"📄 Documento cargado: **{nombre_pdf}**")

# 3. Instrucciones del sistema
system_instruction = (
    "Eres un asistente virtual de atención y soporte para 'Mercado Central 24h'. "
    "Tu única tarea es resolver dudas y preguntas basándote EXCLUSIVAMENTE "
    "en el documento de reglamento, políticas y procedimientos que se te ha proporcionado. "
    "Si la respuesta no se encuentra en el documento, debes indicar amablemente "
    "que la información no está disponible en las políticas oficiales."
)

# 4. Historial del chat en Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Entrada del usuario por la interfaz web
if prompt := st.chat_input("Escribe tu pregunta aquí..."):
    # Guardar y mostrar pregunta del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Preparar la consulta a Gemini
    prompt_completo = f"""
{system_instruction}

[DOCUMENTO DE REFERENCIA]
{document_text[:15000]}
[FIN DEL DOCUMENTO]

Pregunta del usuario: {prompt}
"""

    # Generar y mostrar respuesta
    with st.chat_message("assistant"):
        with st.spinner("Buscando en la documentación..."):
            try:
                response = client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=prompt_completo
                )
                respuesta_texto = response.text
                st.markdown(respuesta_texto)
                st.session_state.messages.append({"role": "assistant", "content": respuesta_texto})
            except Exception as e:
                st.error(f"Error al generar la respuesta: {e}")

