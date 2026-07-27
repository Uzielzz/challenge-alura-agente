import os 
from dotenv import load_dotenv
import os
import sys
from google import genai
from pypdf import PdfReader
# Carga  las variables del archivo .env
load_dotenv()
# Obtiene la API key de forma segura
api_key = os.getenv("GEMINI_API_KEY")
print("INICIANDO SCRIPT")
# Configurar la API key usando la variable cargada
client = genai.Client(api_key=api_key)
# Cargar y leer el documento PDF
pdf_path = "Reglamento.pdf"
print(f"Cargando el documento: {pdf_path}...")
try:
   reader = PdfReader(pdf_path)
   document_text = ""
   for page in reader.pages:
    text = page.extract_text()
   if text:
    document_text += text + "\n"
   print("¡Documento cargado y procesado exitosamente!\n")
   document_text = document_text[:500]
except Exception as e:
 print(f"Error al leer el archivo PDF: {e}")
 sys.exit(1)
# Definir las instrucciones del sistema
system_instruction = (
"Eres un asistente virtual de atención y soporte para 'Mercado Central 24h'. "
"Tu única tarea es resolver dudas y preguntas basándote EXCLUSIVAMENTE "
"en el documento de reglamento y procedimientos que se te ha proporcionado. "
"Si la respuesta no se encuentra en el documento, debes indicar amablemente "
"que la información no está disponible en las políticas oficiales."
)
model = "gemini-flash-latest"
print("CHATBOT DE TERMINAL INICIADO")
print("Escribe tu pregunta sobre el documento. Escribe 'salir' para terminar.\n")
# Bucle interactivo de la terminal
while True:
 try:
   user_input = input("Tú: ")
   if user_input.lower() in ["salir", "exit", "quit"]:
    print("¡Hasta luego!")
    break
   if not user_input.strip():
    continue
   prompt_completo = f"""
   [DOCUMENTO DE REFERENCIA]
   {document_text}
   [FIN DEL DOCUMENTO]
   Pregunta del usuario: {user_input}
   """
   response = client.models.generate_content(model=model , contents=prompt_completo)
   print(f"\nAgente: {response.text}\n" + "-"*40)
 except Exception as e:
    import traceback
    traceback.print_exc()
