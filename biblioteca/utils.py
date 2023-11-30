import smtplib
from email.message import EmailMessage

def send_email(title, content, email):
    EMAIL = 'm.amaral8998@gmail.com'
    PASSWORD = 'mytdpyehnqxkzjcc'

    msg = EmailMessage()

    msg['Subject'] = title
    msg['From'] = EMAIL
    msg['To'] = email

    msg.set_content(content)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)