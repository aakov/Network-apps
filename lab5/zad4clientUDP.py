import socket
import time

server_address = '212.182.24.27'
server_port = 2912

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = b'Test wiadomości UDP'
start_time = time.time()
client_socket.sendto(message, (server_address, server_port))

data, server = client_socket.recvfrom(1024)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Czas przesyłu pakietu UDP: {elapsed_time:.6f} sekund")

client_socket.close()
