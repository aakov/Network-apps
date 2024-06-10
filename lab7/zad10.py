import poplib
import email

server = 'interia.pl'
port = 110
user = 'pasinf2017@infumcs.edu'
password = 'P4SInf2017'

mail = poplib.POP3(server)
mail.user(user)
mail.pass_(password)

num_messages = len(mail.list()[1])

for i in range(num_messages):
    response, lines, octets = mail.retr(i + 1)
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = email.message_from_string(msg_content)

    print(f"Wiadomość {i + 1}:")
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            print(part.get_payload(decode=True).decode('utf-8'))
        elif part.get_content_type() == 'text/html':
            print(part.get_payload(decode=True).decode('utf-8'))

mail.quit()
