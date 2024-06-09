import socket

server_ip = '127.0.0.1'
server_port = 2900

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))


try:
    while True:
        message, client_address = server_socket.recvfrom(1024)
        ip_address = message.decode()

        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            hostname = "Nie znaleziono nazwy dla podanego adresu IP"

        server_socket.sendto(hostname.encode(), client_address)
except KeyboardInterrupt:
    server_socket.close()
    print("Serwer został zamknięty")
