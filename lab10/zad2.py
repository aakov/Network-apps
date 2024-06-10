import socket
from base64 import b64encode
from hashlib import sha1
import os

HOST = 'echo.websocket.org'
PORT = 80
ADDR = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)

handshake = (
    "GET / HTTP/1.1\r\n"
    "Host: {}\r\n"
    "Upgrade: websocket\r\n"
    "Connection: Upgrade\r\n"
    "Sec-WebSocket-Key: {}\r\n"
    "Sec-WebSocket-Version: 13\r\n"
    "\r\n"
)

sec_websocket_key = b64encode(os.urandom(16)).decode('utf-8')
request = handshake.format(HOST, sec_websocket_key)
sock.send(request.encode())

response = sock.recv(1024).decode()

magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
accept_key = b64encode(sha1((sec_websocket_key + magic_string).encode()).digest()).decode('utf-8')
if "Sec-WebSocket-Accept: " + accept_key in response:
    print("Handshake successful")
    message = "Hello, WebSocket!"
    frame = bytearray([0x81, len(message)]) + message.encode()
    sock.sendall(frame)

    echo_response = sock.recv(1024)
    print("Received echo:", echo_response.decode())
    sock.close()
else:
    print("Handshake failed")
