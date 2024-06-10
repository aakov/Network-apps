import socket
import ssl
import base64

server = 'interia.pl'
port = 110
username = 'pasinf2017@infumcs.edu'
password = 'P4SInf2017'

def connect_to_pop3(server, port, username, password):
    context = ssl.create_default_context()
    connection = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=server)
    connection.connect((server, port))
    response = connection.recv(4096).decode()
    print(response)

    connection.sendall(f'USER {username}\r\n'.encode())
    response = connection.recv(4096).decode()
    print(response)

    connection.sendall(f'PASS {password}\r\n'.encode())
    response = connection.recv(4096).decode()
    print(response)

    return connection

def show_largest_message(connection):
    connection.sendall(b'LIST\r\n')
    response = connection.recv(4096).decode()
    print(response)

    lines = response.split('\r\n')
    largest_size = 0
    largest_msg_num = 0
    for line in lines[1:]:
        if line == '.':
            break
        parts = line.split(' ')
        msg_num = int(parts[0])
        size = int(parts[1])
        if size > largest_size:
            largest_size = size
            largest_msg_num = msg_num

    if largest_msg_num > 0:
        connection.sendall(f'RETR {largest_msg_num}\r\n'.encode())
        response = connection.recv(4096).decode()
        print(response)

def main():
    connection = connect_to_pop3(server, port, username, password)
    show_largest_message(connection)
    connection.sendall(b'QUIT\r\n')
    connection.close()

