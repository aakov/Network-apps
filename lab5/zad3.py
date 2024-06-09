import socket

server_ip = '212.182.24.27'
server_port = 2913

udp_ports_sequence = [6661, 6662, 6663]

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for port in udp_ports_sequence:
    udp_socket.sendto(b'PING', (server_ip, port))

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp_socket.connect((server_ip, server_port))
    message = tcp_socket.recv(1024)
    print(f'Otrzymana wiadomość: {message.decode()}')
except Exception as e:
    print(f'Błąd połączenia: {e}')
finally:
    udp_socket.close()
    tcp_socket.close()
