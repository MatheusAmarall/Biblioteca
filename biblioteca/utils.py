import smtplib
from email.message import EmailMessage

def send_email(title, msg, email):
    EMAIL = 'm.amaral8998@gmail.com'
    PASSWORD = 'tpogflrfijaudmqo'

    msg = EmailMessage()

    msg['Subject'] = title
    msg['From'] = EMAIL
    msg['To'] = email

    msg.set_content(msg)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)