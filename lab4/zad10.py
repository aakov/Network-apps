import socket

def parse_message(message, src_port, dst_port):
    try:
        parts = message.split(';')
        if len(parts) != 7:
            return "BAD SYNTAX"

        if parts[0] != "zad13odp" or parts[1] != "src" or parts[3] != "dst" or parts[5] != "data":
            return "BAD SYNTAX"

        if int(parts[2]) != src_port or int(parts[4]) != dst_port:
            return "BAD SYNTAX"

        data = parts[6]

        return "TAK"
    except Exception as e:
        return "BAD SYNTAX"

host='127.0.0.1' 
port=2900
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((host, port))
    print(f"Serwer nasłuchuje na {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        src_port = client_address[1]
        dst_port = port

        print(f"Odebrano wiadomość: {message} od {client_address}")

        response = parse_message(message, src_port, dst_port)
        print(f"Wysłano odpowiedź: {response}")
        server_socket.sendto(response.encode(), client_address)



