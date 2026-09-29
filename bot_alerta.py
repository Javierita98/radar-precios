import os
import requests

# GitHub Secrets inyectará estas llaves de forma segura
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
THREAD_ID = os.environ.get('TELEGRAM_THREAD_ID')

def enviar_alerta():
    mensaje = (
        "🚨 <b>RADAR DE PRECIOS - ALERTA AUTOMÁTICA</b> 🚨\n\n"
        "✨ ¡Prueba de GitHub Actions exitosa!\n"
        "Este mensaje se envió solo, sin servidor ni consola abierta, directo a tu tema."
    )
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": mensaje,
        "parse_mode": "HTML"
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("¡Alerta enviada con éxito a Telegram!")
    else:
        print(f"Error al enviar: {response.text}")

if __name__ == "__main__":
    enviar_alerta()
