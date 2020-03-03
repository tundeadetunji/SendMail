import smtplib
import ssl
from email.message import EmailMessage

class SendMail:
    def __init__(self, from_email, from_email_password, to_email, subject, email_text, port=465, smtp_server="smtp.gmail.com"):
        self._from_email = from_email
        self._from_email_password = from_email_password
        self._to_email = to_email
        self._subject = subject
        self._email_text = email_text
        self._port = port
        self._smtp_server = smtp_server


    def SendEmail(self):
        msg = EmailMessage()
        msg.set_content(self._email_text)

        msg['Subject'] = self._subject
        msg['From'] = self._from_email
        msg['To'] = self._to_email

        server = smtplib.SMTP_SSL(self._smtp_server, self._port)
        server.login(self._from_email, self._from_email_password)
        server.send_message(msg)
        server.quit()


