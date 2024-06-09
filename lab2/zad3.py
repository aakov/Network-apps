import socket

def tcp_client(server_ip, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect((server_ip, server_port))

        while True:
            message = input("Wpisz wiadomość do wysłania : ")

            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode('utf-8'))
            print(f"Wysłano wiadomość: {message}")

            response = client_socket.recv(4096)
            print(f"Odebrano odpowiedź: {response.decode('utf-8')}")

    except Exception as e:
        print(f"Błąd: {e}")

    finally:
        client_socket.close()
        print("Połączenie zostało zamknięte")

server_ip = '212.182.24.27'
server_port = 2900
tcp_client(server_ip, server_port)
