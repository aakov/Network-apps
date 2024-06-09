import socket

server_address = '212.182.24.27'
port = 2901

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        message = input("Wpisz wiadomość do wysłania (lub 'exit' aby zakończyć): ")

        if message.lower() == 'exit':
            break

        print(f"Wysyłanie wiadomości do serwera {server_address}:{port}")
        sock.sendto(message.encode(), (server_address, port))

        data, server = sock.recvfrom(4096)
        print(f"Otrzymano odpowiedź: {data.decode()}")

finally:
    print("Zamykanie gniazda")
    sock.close()
