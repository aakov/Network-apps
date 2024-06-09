import socket

host = '127.0.0.1'
port = 2900
max_length = 20


def ensure_length(data, length):
    return data.ljust(length)[:length]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Połączono z {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data = ensure_length(data.decode(), max_length).encode()
            conn.sendall(data)
