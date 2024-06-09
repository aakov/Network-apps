import socket

server_address = '127.0.0.1'
server_port = 2900

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, server_port))


try:
    while True:
        hostname, client_address = server_socket.recvfrom(1024)
        hostname = hostname.decode('utf-8')
        print(f"Otrzymano nazwę hosta: {hostname} od {client_address}")

        try:
            ip_address = socket.gethostbyname(hostname)
            server_socket.sendto(ip_address.encode('utf-8'), client_address)
            print("Sent")
        except socket.error as e:
            error_message = "Nie znaleziono IP"
            server_socket.sendto(error_message.encode('utf-8'), client_address)
finally:
    server_socket.close()
