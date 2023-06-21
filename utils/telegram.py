import requests
from dotenv                                                 import load_dotenv
import os
load_dotenv()


class TelegramUtils:

    def enviarAlerta(mensagem):
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        token = os.getenv("TELEGRAM_TOKEN")
        if token != "" and chat_id != "":
            url = f"https://api.telegram.org/bot{token}/sendMessage"

            data = {
                "chat_id": chat_id,
                "text": f"ℹ️ {mensagem}" 
            }

            response = requests.post(url, data=data)

            if response.status_code == 200:
                print("✉️ Mensagem enviada para o Telegram com sucesso!")
            else:
                print("❌ Falha ao enviar mensagem para o Telegram.")