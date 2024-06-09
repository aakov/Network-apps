import socket

def tcp_client(server_ip, server_port, message):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))

        if len(message) < 20:
            message = message.ljust(20)
        elif len(message) > 20:
            message = message[:20]

        total_sent = 0
        while total_sent < len(message):
            sent = client_socket.send(message[total_sent:].encode('utf-8'))
            if sent == 0:
                raise RuntimeError("Wysłanie niepowiodło się")
            total_sent += sent

        received_data = b''
        while len(received_data) < 20:
            chunk = client_socket.recv(20 - len(received_data))
            if not chunk:
                raise RuntimeError("Odbieranie niepowiodło się")
            received_data += chunk

        print(f"Odpowiedź: {received_data.decode('utf-8')}")

    except Exception as e:
        print(f"Błąd: {e}")

    finally:
        client_socket.close()

server_ip = '212.182.24.27'
server_port = 2908
message = "Hello, Server!"
tcp_client(server_ip, server_port, message)
