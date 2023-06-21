import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
load_dotenv()


class EmailUtils:

    def enviarAlerta(message):

        EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")
        SMTP_EMAIL = os.getenv("SMTP_EMAIL")
        SMTP_SERVER = os.getenv("SMTP_SERVER")
        SMTP_PORT = int(os.getenv("SMTP_PORT"))
        SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

        if EMAIL_RECIPIENT != "" and SMTP_EMAIL != "" and SMTP_SERVER != "" and SMTP_PORT != "" and SMTP_PASSWORD != "":

            message = MIMEMultipart("alternative")
            message["Subject"] = "Alerta de renovação de Dominio"
            message["From"] = SMTP_EMAIL
            message["To"] = EMAIL_RECIPIENT
            text = "Use um navegador compativel com HTML5"

            # Turn these into plain/html MIMEText objects
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(message, "html")

            message.attach(part1)
            message.attach(part2)


            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

                server.starttls()
                server.login(SMTP_EMAIL, SMTP_PASSWORD)
                server.sendmail(SMTP_EMAIL, EMAIL_RECIPIENT,
                                message.as_string().encode("latin1"))
                server.quit()
