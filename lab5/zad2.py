import socket
import random

host = '127.0.0.1'
port = 2912
server_address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

secret_number = random.randint(1, 100)
print(f"Wylosowana liczba to: {secret_number}")

try:
    client_socket, client_address = server_socket.accept()
    print(f"Połączenie z {client_address}")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        try:
            client_number = int(data)
            if client_number < secret_number:
                response = "mniejsza"
            elif client_number > secret_number:
                response = "większa"
            else:
                response = "równa"
                print("Klient odgadł liczbę!")
                break
        except ValueError:
            response = "błąd"

        client_socket.sendall(response.encode())

finally:
    client_socket.close()
    server_socket.close()
