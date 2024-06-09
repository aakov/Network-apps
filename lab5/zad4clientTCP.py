import socket
import time

server_address = '212.182.24.27'
server_port = 2912

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, server_port))

message = b'Test wiadomości TCP'
start_time = time.time()
client_socket.sendall(message)

data = client_socket.recv(1024)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Czas przesyłu pakietu TCP: {elapsed_time:.6f} sekund")

client_socket.close()
