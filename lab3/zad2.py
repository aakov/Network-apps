import socket

tcp_segment_hex = '0b54898b1f9a18ecbbb164f2801800e3677100000101080a02c1a4ee001a4cee68656c6c6f203a29'

tcp_segment_bytes = bytes.fromhex(tcp_segment_hex)

src_port = int(tcp_segment_hex[0:4], 16)
dst_port = int(tcp_segment_hex[4:8], 16)
data_offset = int(tcp_segment_hex[24:25], 16) * 4
data = tcp_segment_bytes[data_offset:]

message = f'zad13odp;src;{src_port};dst;{dst_port};data;{data.decode()}'

server_address = ('212.182.24.27', 2909)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.sendto(message.encode(), server_address)

    response, _ = sock.recvfrom(4096)
    print(f'Odpowiedź serwera: {response.decode()}')
finally:
    sock.close()
