# Verificador de Expiração de Domínio

Este script verifica a data de expiração de uma lista de domínios e envia alertas via Telegram com base na proximidade da data de expiração. Ele utiliza a biblioteca `python-whois` para obter informações sobre os domínios.

## Funcionamento

O script possui uma lista de domínios. Ele percorre cada domínio e utiliza a biblioteca `python-whois` para obter a data de expiração do domínio. Em seguida, calcula a quantidade de dias restantes até a expiração e envia alertas via Telegram de acordo com a proximidade da data.

O script utiliza a função `verificar_expiracao()` para verificar a expiração de cada domínio e enviar alertas. A função `enviarAlerta()` é responsável por enviar as mensagens via API do Telegram.

## Requisitos

- Python 3.x
- Biblioteca `python-whois`
- Biblioteca `python-dotenv`

## Instalação

1. Certifique-se de ter o Python 3.x instalado em seu sistema.

2. Instale as bibliotecas `python-whois` e `python-dotenv` utilizando o comando pip:

```
pip install python-whois python-dotenv
```

## Utilização

1. Abra o arquivo `verificador.py` em um editor de texto.

2. Insira os domínios que você deseja verificar no arquivo `verificador.py`. Procure pela seção onde é definido o array `dominio1`, `dominio2`, etc., e substitua-os pelos domínios desejados.

3. Configure as informações de alertas no arquivo `.env`. Abra o arquivo `.env` em um editor de texto e preencha as configurações de alertas conforme necessário. 

   Exemplo de arquivo `.env`:
   ```
TELEGRAM_TOKEN=<SEU_TOKEN_DO_TELEGRAM>
TELEGRAM_CHAT_ID=<SEU_CHAT_ID_DO_TELEGRAM>""

SMTP_EMAIL=<SEU_EMAIL_PARA_ENVIO_SMTP>
SMTP_SERVER=<SEU_SERVIDOR_DE_EMAIL>
SMTP_PORT=<SUA_PORTA_SMTP>
SMTP_PASSWORD=<SUA_SENHA_SMTP>
EMAIL_RECIPIENT=<EMAIL_DE_QUEM_RECEBERA_EMAILS>

URL_WEBHOOK=<SUA_URL_DE_WEBHOOK>
   ```

Certifique-se de substituir pelos valores corretos.

4. Execute o script com o comando:
```
python verificador.py
```

## Observações

- Certifique-se de que o seu sistema possui conexão com a internet para que o script possa obter informações dos domínios.

- O script já possui uma lista de domínios de exemplo. Você pode modificar essa lista de acordo com as suas necessidades, adicionando ou removendo domínios.

- Os alertas são enviados para um chat ou grupo específico do Telegram. Certifique-se de fornecer o ID do chat correto na variável `chat_id` da função `enviarAlerta()`.

- Os dias para envio dos alertas podem ser ajustados modificando as condições dentro da função `verificar_expiracao()`.