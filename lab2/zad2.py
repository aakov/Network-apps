import socket

def tcp_client(server_ip, server_port, message):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        client_socket.sendall(message.encode('utf-8'))
        response = client_socket.recv(4096)
        print(f" Odpowiedź: {response.decode('utf-8')}")

    except Exception as e:
        print(f"Błąd: {e}")

    finally:
        client_socket.close()


server_ip = '127.182.24.27'
server_port = 2900
message = "Hello, Server!"
tcp_client(server_ip, server_port, message)
