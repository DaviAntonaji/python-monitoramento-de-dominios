# Verificador de Expiração de Domínio

Este script verifica a data de expiração de uma lista de domínios e envia alertas via Telegram com base na proximidade da data de expiração. Ele utiliza a biblioteca `python-whois` para obter informações sobre os domínios.

## Funcionamento

O script possui uma lista de dominios. Ele percorre cada domínio e utiliza a biblioteca `python-whois` para obter a data de expiração do domínio. Em seguida, calcula a quantidade de dias restantes até a expiração e envia alertas via Telegram de acordo com a proximidade da data.

O script utiliza a função `verificar_expiracao()` para verificar a expiração de cada domínio e enviar alertas. A função `enviarAlerta()` é responsável por enviar as mensagens via API do Telegram.

## Requisitos

- Python 3.x
- Biblioteca `python-whois`

## Instalação

1. Certifique-se de ter o Python 3.x instalado em seu sistema.

2. Instale a biblioteca `python-whois` utilizando o comando pip:

```
pip install python-whois
```

## Utilização

1. Abra o arquivo `verificador.py` em um editor de texto.

2. Insira as informações de autenticação da API do Telegram na função `enviarAlerta()`. Você precisará substituir a variável `token` e `chat_id` com o seu token e chat_id do Telegram.

3. Execute o script com o comando:
```
python verificador.py
```

## Observações

- Certifique-se de que o seu sistema possui conexão com a internet para que o script possa obter informações dos domínios.

- O script já possui uma lista de domínios de exemplo. Você pode modificar essa lista de acordo com as suas necessidades, adicionando ou removendo  domínios.

- Os alertas são enviados para um chat ou grupo específico do Telegram. Certifique-se de fornecer o ID do chat correto na variável `chat_id` da função `enviarAlerta()`.

- Os dias para envio dos alertas podem ser ajustados modificando as condições dentro da função `verificar_expiracao()`.

