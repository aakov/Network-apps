import socket

server_address = '212.182.24.27'
port = 2901
message = "Hello, Server!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    print(f"Wysyłanie wiadomości do serwera {server_address}:{port}")
    sent = sock.sendto(message.encode(), (server_address, port))
    data, server = sock.recvfrom(4096)
    print(f"Otrzymano odpowiedź: {data.decode()}")

finally:
    sock.close()
