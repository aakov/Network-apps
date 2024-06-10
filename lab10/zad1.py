import socket
from base64 import b64encode
import os

HOST = 'echo.websocket.org'
PORT = 80
RESOURCE = '/'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

handshake_request = (
    f'GET {RESOURCE} HTTP/1.1\r\n'
    f'Host: {HOST}\r\n'
    f'Upgrade: websocket\r\n'
    f'Connection: Upgrade\r\n'
    f'Sec-WebSocket-Key: {b64encode(os.urandom(16)).decode("utf-8")}\r\n'
    f'Origin: http://{HOST}\r\n'
    f'Sec-WebSocket-Protocol: chat\r\n'
    f'Sec-WebSocket-Version: 13\r\n'
    '\r\n'
)
sock.sendall(handshake_request.encode('utf-8'))

response = sock.recv(4096)
print(response.decode('utf-8'))

sock.close()
