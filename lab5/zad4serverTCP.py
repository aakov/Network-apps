import socket
import time

server_address = '0.0.0.0'
server_port = 2912

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_address, server_port))
server_socket.listen(1)

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Połączenie od {client_address}")

    data = client_socket.recv(1024)
    if data:
        start_time = time.time()
        client_socket.sendall(data)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Czas przesyłu pakietu TCP: {elapsed_time:.6f} sekund")

    client_socket.close()
