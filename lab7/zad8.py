import poplib
import re

server = 'interia.pl'
port = 110
username = 'pasinf2017@infumcs.edu'
password = 'P4SInf2017'

mail = poplib.POP3(server)
mail.user(username)
mail.pass_(password)

response, listings, octets = mail.list()
for listing in listings:
    number, size = re.split(b' ', listing)
    print(f"Wiadomość {number.decode('utf-8')} ma rozmiar {size.decode('utf-8')} bajtów.")

mail.quit()
