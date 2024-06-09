import socket
import struct

data = '4500004ef7fa400038069d33d4b6181bc0a800020b54b9a6fbf93c57c10a06c1801800e3ce9c00000101080a03a6eb01000bf8e56e6574776f726b2070726f6772616d6d696e672069732066756e'

packet = bytes.fromhex(data)

version = packet[0] >> 4
ihl = (packet[0] & 15) * 4
src_ip = socket.inet_ntoa(packet[12:16])
dst_ip = socket.inet_ntoa(packet[16:20])
protocol = packet[9]

src_port = struct.unpack('!H', packet[ihl:ihl+2])[0]
dst_port = struct.unpack('!H', packet[ihl+2:ihl+4])[0]
data_offset = ihl + (packet[ihl+12] >> 4) * 4
data_length = len(packet) - data_offset
data_bytes = packet[data_offset:]

messageA = f'zad15odpA;ver;{version};srcip;{src_ip};dstip;{dst_ip};type;{protocol}'
messageB = f'zad15odpB;srcport;{src_port};dstport;{dst_port};data;{data_bytes.hex()}'

server_address = ('212.182.24.27', 2911)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.sendto(messageA.encode(), server_address)
    responseA, _ = sock.recvfrom(1024)
    print('Odpowiedź serwera na wiadomość A:', responseA.decode())

    if responseA.decode() == 'TAK':
        sock.sendto(messageB.encode(), server_address)
        responseB, _ = sock.recvfrom(1024)
        print('Odpowiedź serwera na wiadomość B:', responseB.decode())
