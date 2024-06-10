import socket

host = '127.0.0.1'
port = 110
welcome_message = '+OK POP3 server ready\r\n'

commands = {
    'USER': '+OK user accepted\r\n',
    'PASS': '+OK pass accepted\r\n',
    'STAT': '+OK 0 0\r\n',
    'LIST': '+OK 0 messages:\r\n.\r\n',
    'RETR': '+OK message follows\r\n.\r\n',
    'DELE': '+OK message deleted\r\n',
    'QUIT': '+OK goodbye\r\n'
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f'Serwer POP3 uruchomiony na {host}:{port}')

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Połączenie z {client_address}')
    client_socket.send(welcome_message.encode())

    while True:
        command = client_socket.recv(1024).decode().strip()
        if not command:
            break

        response = commands.get(command[:4].upper(), '-ERR command not implemented\r\n')
        client_socket.send(response.encode())

        if command[:4].upper() == 'QUIT':
            break

    client_socket.close()
