import socket
import time

server_address = '0.0.0.0'
server_port = 2912

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, server_port))


while True:
    data, client_address = server_socket.recvfrom(1024)
    if data:
        start_time = time.time()
        server_socket.sendto(data, client_address)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Czas przesyłu pakietu UDP: {elapsed_time:.6f} sekund")
