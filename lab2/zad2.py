import socket

def client():
    # Adres IP i port serwera
    SERVER_IP = '212.182.24.27'
    SERVER_PORT = 2900

    # Wiadomość do wysłania
    message = "Hello, server! This is a message from the client."

    try:
        # Utwórz socket klienta
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Połącz się z serwerem
        client_socket.connect((SERVER_IP, SERVER_PORT))

        # Wyślij wiadomość do serwera
        client_socket.sendall(message.encode())

        # Odbierz odpowiedź od serwera
        response = client_socket.recv(1024)

        # Wyświetl odpowiedź
        print("Otrzymana odpowiedź od serwera:", response.decode())

        # Zamknij połączenie z serwerem
        client_socket.close()

    except Exception as e:
        print("Wystąpił błąd podczas połączenia z serwerem:", e)

client()
