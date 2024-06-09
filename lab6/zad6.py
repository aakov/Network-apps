import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'interia.pl'
port = 587
user_email = input('Podaj adres email nadawcy: ')
recipient_email = input('Podaj adres email odbiorcy: ')
subject = input('Podaj temat wiadomości: ')
body = input('Wpisz treść wiadomości: ')

message = MIMEMultipart()
message['From'] = user_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(user_email, input('Podaj hasło: '))
server.sendmail(user_email, recipient_email, message.as_string())
server.quit()

print('Wiadomość została wysłana!')
