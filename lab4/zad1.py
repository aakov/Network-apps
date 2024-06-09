import socket
from datetime import datetime

host = '127.0.0.1'
port = 2900

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

try:
    while True:
        client_socket, address = server_socket.accept()
        print("Połączono ")

        _ = client_socket.recv(1024)

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        client_socket.sendall(current_time.encode('utf-8'))

        client_socket.close()

except KeyboardInterrupt:
    print("Closed ")
finally:
    server_socket.close()
