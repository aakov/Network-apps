import socket

server_address = '127.0.0.1'
server_port = 2900

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, server_port))

try:
    while True:
        data, client_address = server_socket.recvfrom(4096)
        print(f"Odebrano wiadomość: {data.decode()} od {client_address}")

        if data:
            sent = server_socket.sendto(data, client_address)
            print(f"Wysłano {sent} bajtów z powrotem do {client_address}")
finally:
    server_socket.close()
