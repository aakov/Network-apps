import poplib
import re

server = 'interia.pl'
port = 110
username = 'pasinf2017@infumcs.edu'
password = 'P4SInf2017'

pop_conn = poplib.POP3(server, port)
pop_conn.user(username)
pop_conn.pass_(password)

response, listings, octets = pop_conn.list()

total_size = sum(int(re.search(r'\d+ (\d+)', listing.decode('utf-8')).group(1)) for listing in listings)

print(f'Łączny rozmiar wiadomości w skrzynce: {total_size} bajtów')

pop_conn.quit()
