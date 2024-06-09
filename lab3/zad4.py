import socket
import wireshark

# Nie wiem czy to trzeba wysylac
def run_client(packet_data):
    client_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM if packet_data['protocol'] == 'TCP' else socket.SOCK_DGRAM)

    try:
        client_socket.connect((packet_data['address'], packet_data['port']))
        client_socket.sendall(packet_data['data'].encode())

        response = client_socket.recv(1024)
        print(f'Odpowiedź od serwera: {response.decode()}')
    finally:
        client_socket.close()



packet_data = {
    'address': '212.182.24.27',
    'port': 2909,
    'data': ' dane do wysłania',
    'protocol': 'TCP'
}

run_client(packet_data)

wireshark.capture(packet_data['address'], packet_data['port'])
