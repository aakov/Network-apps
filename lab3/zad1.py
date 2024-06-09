import socket
import binascii

hex_data = 'ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e'

udp_datagram = binascii.unhexlify(hex_data)

src_port = int(udp_datagram[0:2].hex(), 16)

dst_port = int(udp_datagram[2:4].hex(), 16)

data = udp_datagram[8:].decode('utf-8')

result = f'zad14odp;src;{src_port};dst;{dst_port};data;{data}'

server_address = ('212.182.24.27', 2910)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.sendto(result.encode('utf-8'), server_address)

    response, _ = sock.recvfrom(4096)
    print(f'Odpowiedź serwera: {response.decode("utf-8")}')
finally:
    sock.close()
