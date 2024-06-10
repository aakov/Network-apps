import imaplib

host = '212.182.24.27'
port = 143
username = 'pasumcs@infumcs.edu'
password = 'P4SInf2017'

mail = imaplib.IMAP4(host, port)
mail.login(username, password)

mail.select('inbox')

typ, data = mail.search(None, 'UNSEEN')
for num in data[0].split():
    typ, data = mail.fetch(num, '(BODY[TEXT])')
    print('Treść wiadomości:', data[0][1])

    mail.store(num, '+FLAGS', '\\Seen')

mail.close()
mail.logout()
