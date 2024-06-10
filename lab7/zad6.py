import poplib

server = 'interia.pl'
port = 110
username = 'pasinf2017@infumcs.edu'
password = 'P4SInf2017'

pop_conn = poplib.POP3(server, port)
pop_conn.user(username)
pop_conn.pass_(password)

num_messages = len(pop_conn.list()[1])
print(f"Liczba wiadomości w skrzynce: {num_messages}")

pop_conn.quit()
