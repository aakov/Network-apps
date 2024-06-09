import socket
import base64

def send_email(sender, recipients, subject, body, attachment_filename=None):
    server_address = 'mx.interia.pl'
    server_port = 587

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.sendall(b'EHLO example.com\r\n')
    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.sendall(b'STARTTLS\r\n')
    response = client_socket.recv(1024).decode()
    print(response)

    secure_socket = socket.create_default_context().wrap_socket(client_socket, server_hostname=server_address)

    secure_socket.sendall(b'AUTH LOGIN\r\n')
    response = secure_socket.recv(1024).decode()
    print(response)

    username = base64.b64encode(b'YOUR_EMAIL').decode() + '\r\n'
    secure_socket.sendall(username.encode())
    response = secure_socket.recv(1024).decode()
    print(response)

    password = base64.b64encode(b'YOUR_PASSWORD').decode() + '\r\n'
    secure_socket.sendall(password.encode())
    response = secure_socket.recv(1024).decode()
    print(response)

    secure_socket.sendall(f'MAIL FROM:<{sender}>\r\n'.encode())
    response = secure_socket.recv(1024).decode()
    print(response)

    for recipient in recipients:
        secure_socket.sendall(f'RCPT TO:<{recipient}>\r\n'.encode())
        response = secure_socket.recv(1024).decode()
        print(response)

    secure_socket.sendall(b'DATA\r\n')
    response = secure_socket.recv(1024).decode()
    print(response)

    secure_socket.sendall(f'Subject: {subject}\r\n'.encode())
    secure_socket.sendall(f'From: {sender}\r\n'.encode())
    secure_socket.sendall(f'To: {", ".join(recipients)}\r\n'.encode())
    secure_socket.sendall(b'MIME-Version: 1.0\r\n')

    if attachment_filename:
        secure_socket.sendall(b'Content-Type: multipart/mixed; boundary="===============9009668879624028876=="\r\n')
        secure_socket.sendall(b'\r\n--===============9009668879624028876==\r\n')
        secure_socket.sendall(b'Content-Type: text/plain; charset="utf-8"\r\n')
        secure_socket.sendall(b'\r\n' + body.encode() + b'\r\n')
        secure_socket.sendall(b'\r\n--===============9009668879624028876==\r\n')
        secure_socket.sendall(b'Content-Type: image/jpeg; name="' + attachment_filename.encode() + b'"\r\n')
        secure_socket.sendall(b'Content-Disposition: attachment; filename="' + attachment_filename.encode() + b'"\r\n')
        with open(attachment_filename, 'rb') as attachment_file:
            attachment_content = attachment_file.read()
            secure_socket.sendall(b'\r\n' + attachment_content + b'\r\n')
        secure_socket.sendall(b'\r\n--===============9009668879624028876==--\r\n')
    else:
        secure_socket.sendall(b'\r\n' + body.encode() + b'\r\n')

    secure_socket.sendall(b'.\r\n')
    response = secure_socket.recv(1024).decode()
    print(response)

    secure_socket.sendall(b'QUIT\r\n')
    response = secure_socket.recv(1024).decode()
    print(response)
    secure_socket.close()

sender = input("Podaj adres nadawcy: ")
recipients = input("Podaj adresy odbiorców (oddzielone przecinkami): ").split(',')
subject = input("Podaj temat wiadomości: ")
body = input("Podaj treść wiadomości: ")
attachment_filename = input("Podaj nazwę pliku obrazka załącznika (jeśli brak, pozostaw puste): ")
send_email(sender, recipients, subject, body, attachment_filename)
