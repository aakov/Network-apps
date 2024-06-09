import socket
import struct
import time


def get_ntp_time(host, port=123):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    data = '\x1b' + 47 * '\0'
    client.sendto(data.encode(), (host, port))
    data, _ = client.recvfrom(1024)
    client.close()
    ntp_time = struct.unpack('!12I', data)[10] - 2208988800
    return time.ctime(ntp_time)

ntp_server = 'ntp.task.gda.pl'
ntp_port = 123

current_time = get_ntp_time(ntp_server, ntp_port)
print("Aktualna data i czas :", current_time)
