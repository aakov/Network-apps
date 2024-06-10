import imaplib

host = '212.182.24.27'
port = 143
username = 'pasinf2017@infumcs.edu'
password = 'P4SInf2017'

mail = imaplib.IMAP4(host, port)
mail.login(username, password)
mail.select('Inbox')

typ, data = mail.search(None, 'ALL')
message_ids = data[0].split()
message_count = len(message_ids)

print(f'Liczba wiadomości w skrzynce Inbox: {message_count}')

mail.logout()
