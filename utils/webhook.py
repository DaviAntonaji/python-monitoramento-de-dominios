import requests
from dotenv                                                 import load_dotenv
import os
load_dotenv()


class WebhookUtils:

    def enviarAlerta(mensagem):
        URL_WEBHOOK = os.getenv("URL_WEBHOOK")
        if URL_WEBHOOK != "":
            data = {"message": mensagem}
            response = requests.post(URL_WEBHOOK, data=data)

            if response.status_code == 200:
                print("✉️ Mensagem enviada para o Webhook com sucesso!")
            else:
                print("❌ Falha ao enviar mensagem para o Webhook.")