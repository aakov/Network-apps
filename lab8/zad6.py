import socket

host = '127.0.0.1'
port = 143

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f'Serwer IMAP nasłuchuje na {host}:{port}')


def handle_imap_command(command, client_socket):
    if command.startswith('A1 LOGIN'):
        response = '+ OK Logged in\r\n'
    elif command.startswith('A1 LOGOUT'):
        response = '+ OK Logout completed\r\n'
    elif command.startswith('A1 LIST'):
        response = '* LIST (\HasNoChildren) "/" INBOX\r\n+ OK List completed\r\n'
    elif command.startswith('A1 SELECT'):
        response = '+ OK Select completed\r\n'
    else:
        response = '- BAD Command not recognized\r\n'
    client_socket.send(response.encode('utf-8'))


try:
    while True:
        client_socket, address = server_socket.accept()
        print(f'Połączenie z {address}')
        client_socket.send('* OK IMAP server ready\r\n'.encode('utf-8'))

        while True:
            command = client_socket.recv(1024).decode('utf-8').strip()
            if not command:
                break
            print(f'Otrzymano komendę: {command}')
            handle_imap_command(command, client_socket)

        client_socket.close()
except KeyboardInterrupt:
    print('Zamykanie serwera...')
finally:
    server_socket.close()
