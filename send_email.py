from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import getpass
import keyring


def send_email(send_from: str, send_to: list, cc_to: list, subject: str, text, name: str, file=None):
    msg = MIMEMultipart('alternative')
    msg['From'] = send_from
    msg['To'] = '; '.join(send_to)
    msg['CC'] = '; '.join(cc_to)
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'html'))

    if file:
        attachment = MIMEApplication(open(file, 'rb').read(), Name=name)
        attachment['Content-Disposition'] = 'attachment;'
        msg.attach(attachment)

    s = smtplib.SMTP('host.name', port=0)
    s.ehlo()
    s.set_debuglevel(2)
    s.starttls()
    # configure credentials with getpass and keyring
    s.login(user='username', password='password')
    s.sendmail(send_from, send_to, msg.as_string())
    s.quit()
    print('email sent')
