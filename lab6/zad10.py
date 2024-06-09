import socket

class SMTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Nowe połączenie od: {client_address}")

            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        client_socket.send(b'220 localhost Simple Mail Transfer Service Ready\r\n')

        while True:
            request = client_socket.recv(1024).decode().strip()
            print(f"Otrzymano: {request}")

            if request.startswith('EHLO') or request.startswith('HELO'):
                client_socket.send(b'250 localhost\r\n')
            elif request.startswith('MAIL FROM:'):
                client_socket.send(b'250 Ok\r\n')
            elif request.startswith('RCPT TO:'):
                client_socket.send(b'250 Ok\r\n')
            elif request == 'DATA':
                client_socket.send(b'354 Start mail input; end with <CRLF>.<CRLF>\r\n')
                message_data = b''
                while True:
                    data = client_socket.recv(1024)
                    message_data += data
                    if data.endswith(b'\r\n.\r\n'):
                        break
                client_socket.send(b'250 Ok: queued as 12345\r\n')
            elif request == 'QUIT':
                client_socket.send(b'221 Bye\r\n')
                break
            else:
                client_socket.send(b'500 Command unrecognized\r\n')

        client_socket.close()

server = SMTPServer('127.0.0.1', 25)
server.start()
