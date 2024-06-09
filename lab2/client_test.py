import socket

def simple_client(server_ip, server_port, message):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        client_socket.sendall(message.encode('utf-8'))
        response = client_socket.recv(1024)
        print(f"Response: {response.decode('utf-8')}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

server_ip = '127.0.0.1'
server_port = 2900
message = "Hello, Simple Server!"
simple_client(server_ip, server_port, message)
