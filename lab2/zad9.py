import socket

server_address = ('212.182.24.27', 2906)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    ip_address = input("Podaj adres IP: ")
    client_socket.sendto(ip_address.encode(), server_address)

    hostname, server_address = client_socket.recvfrom(1024)
    print("Otrzymana nazwa hosta:", hostname.decode())

finally:
    client_socket.close()
