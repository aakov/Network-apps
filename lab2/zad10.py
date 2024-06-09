import socket

server_address = ('212.182.24.27', 2907)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    hostname = input("Podaj nazwę hosta: ")

    client_socket.sendto(hostname.encode(), server_address)

    ip_address, server_address = client_socket.recvfrom(1024)
    print("Otrzymany adres IP:", ip_address.decode())

finally:
    client_socket.close()
