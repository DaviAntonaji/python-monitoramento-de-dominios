import whois
from datetime import datetime, timedelta
import requests

dominios = ["antonaji.com.br", "google.com", ]

def enviarAlerta(mensagem):
    chat_id = ""
    token = ""
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

def verificar_expiracao(dominio, cliente):
    print(f"Verificando o domínio: {dominio}")

    w = whois.whois(dominio)

    data_expiracao = w.expiration_date

    if isinstance(data_expiracao, list):
        data_expiracao = data_expiracao[0]

    dias_restantes = (data_expiracao - datetime.now()).days

    if dias_restantes > 30:
        print(f"O domínio {dominio} expira em {dias_restantes} dias. Portanto, está OK.")

    elif dias_restantes == 30:
        enviarAlerta(f"📅 O domínio {dominio}  expira em {dias_restantes} dias. Ainda há tempo para renovar.")
    elif dias_restantes == 15:
        enviarAlerta(f"📅 O domínio {dominio}  expira em {dias_restantes} dias. É recomendado renovar em breve.")
    elif dias_restantes == 7:
        enviarAlerta(f"📅 O domínio {dominio}  expira em {dias_restantes} dias. Renove o domínio o mais rápido possível.")
    elif dias_restantes == 3:
        enviarAlerta(f"📅‼️ O domínio {dominio}  expira em {dias_restantes} dias. A renovação é urgente.")
    elif dias_restantes <= 3 and dias_restantes > 0:
        enviarAlerta(f"⚠️⚠️ ALERTA CRÍTICO: O domínio {dominio}  expira em {dias_restantes} dias. Renove imediatamente!")
    else:
        enviarAlerta(f"☠️☠️ ALERTA CRÍTICO: O domínio {dominio}  expirou a {-dias_restantes} dias. Renove imediatamente!!")

    for dominio in dominios:
        verificar_expiracao(dominio)
        print("-----------------------")