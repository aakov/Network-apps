import socket

server_address = '127.0.0.1'
server_port = 2900

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, server_port))


try:
    while True:
        message, client_address = server_socket.recvfrom(1024)
        print(f"Odebrano wiadomość od {client_address}: {message.decode()}")

        if message.decode().startswith('zad13odp;src;') and message.decode().count(';') == 5:
            response = 'TAK'
        else:
            response = 'BAD SYNTAX'

        server_socket.sendto(response.encode(), client_address)
        print(f"Wysłano odpowiedź do {client_address}: {response}")

except KeyboardInterrupt:
    print("Zamykanie serwera...")
    server_socket.close()
