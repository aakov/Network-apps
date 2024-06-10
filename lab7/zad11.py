import poplib
import email
import base64

server = 'interia.pl'
port = 110
user = 'pasinf2017@infumcs.edu'
password = 'P4SInf2017'

mail = poplib.POP3(server)
mail.user(user)
mail.pass_(password)

numMessages = len(mail.list()[1])

for i in range(numMessages):
    raw_email = b"\n".join(mail.retr(i+1)[1])
    parsed_email = email.message_from_bytes(raw_email)

    for part in parsed_email.walk():
        if part.get_content_maintype() == 'multipart' or part.get('Content-Disposition') is None:
            continue

        file_name = part.get_filename()
        if file_name:
            file_data = base64.b64decode(part.get_payload())
            file_path = f"./{file_name}"
            with open(file_path, 'wb') as file:
                file.write(file_data)
            print(f"Załącznik {file_name} został zapisany na dysku.")

mail.quit()
