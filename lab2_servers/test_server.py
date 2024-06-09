import socket

HOST = '127.0.0.1'
PORT = 2900

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Simple server is waiting for incoming connections...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024)
if data:
    print(f"Received: {data.decode('utf-8')}")
    conn.sendall(data)

conn.close()
server_socket.close()
