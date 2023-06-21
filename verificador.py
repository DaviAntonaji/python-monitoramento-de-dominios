import whois
from datetime import datetime, timedelta
import requests
from utils.telegram import TelegramUtils



def verificar_expiracao(dominio):
    print(f"Verificando o domínio: {dominio}")

    w = whois.whois(dominio)

    data_expiracao = w.expiration_date

    if isinstance(data_expiracao, list):
        data_expiracao = data_expiracao[0]

    dias_restantes = (data_expiracao - datetime.now()).days

    if dias_restantes > 30:
        print(f"O domínio {dominio} expira em {dias_restantes} dias. Portanto, está OK.")

    elif dias_restantes == 30:
        TelegramUtils.enviarAlerta(f"📅 O domínio {dominio}  expira em {dias_restantes} dias. Ainda há tempo para renovar.")
    elif dias_restantes == 15:
        TelegramUtils.enviarAlerta(f"📅 O domínio {dominio}  expira em {dias_restantes} dias. É recomendado renovar em breve.")
    elif dias_restantes == 7:
        TelegramUtils.enviarAlerta(f"📅 O domínio {dominio}  expira em {dias_restantes} dias. Renove o domínio o mais rápido possível.")
    elif dias_restantes == 3:
        TelegramUtils.enviarAlerta(f"📅‼️ O domínio {dominio}  expira em {dias_restantes} dias. A renovação é urgente.")
    elif dias_restantes <= 3 and dias_restantes > 0:
        TelegramUtils.enviarAlerta(f"⚠️⚠️ ALERTA CRÍTICO: O domínio {dominio}  expira em {dias_restantes} dias. Renove imediatamente!")
    else:
        TelegramUtils.enviarAlerta(f"☠️☠️ ALERTA CRÍTICO: O domínio {dominio}  expirou a {-dias_restantes} dias. Renove imediatamente!!")

dominios = ["antonaji.com.br", "google.com"]
for dominio in dominios:
    verificar_expiracao(dominio)
    print("-----------------------")
