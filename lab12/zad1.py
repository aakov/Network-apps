import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection

    def run(self):
        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            self.connection.sendall(data)
        self.connection.close()

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(5)
        print(f"Serwer nasłuchuje na {self.ip}:{self.port}")
        try:
            while True:
                connection, address = self.server_socket.accept()
                print(f"Połączono z {address}")
                client_thread = ClientThread(connection)
                client_thread.start()
        except socket.error as e:
            print(f"Błąd gniazda: {e}")
        finally:
            self.server_socket.close()


server = Server('127.0.0.1', 2900)
server.run()
