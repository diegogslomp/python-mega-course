from email.mime.text import MIMEText
import smtplib

def send_mail(email, height):
    from_email = 'example@gmail.com'
    from_password = 'pass'
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>." % height

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
