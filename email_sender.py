import smtplib
import os
import ssl
from email.message import EmailMessage
from word_test import *

def send_mail():
    sender = os.getenv('EMAIL_ADDRESS')
    password = os.getenv('GOOGLE_APP_PASSWORD')
    email_lst = emails()
    subject, body = content()
    for email in email_lst:
        em = EmailMessage()
        em['From'] = sender
        em['To'] = email
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender,password)
            smtp.sendmail(sender,email,em.as_string())

send_mail()