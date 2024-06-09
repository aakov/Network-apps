import socket
import threading
import datetime

def log_event(message):
    with open("server_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

class ClientThread(threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address

    def run(self):
        log_event(f"Połączono z klientem {self.address}")
        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            self.connection.sendall(data)
        self.connection.close()
        log_event(f"Zakończono połączenie z klientem {self.address}")

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(5)
        log_event(f"Serwer działa na {self.ip}:{self.port}")
        print(f"Serwer działa na {self.ip}:{self.port}")
        try:
            while True:
                connection, address = self.server_socket.accept()
                log_event(f"Połączono z {address}")
                print(f"Połączono z {address}")
                client_thread = ClientThread(connection, address)
                client_thread.start()
        except socket.error as e:
            log_event(f"Błąd gniazda: {e}")
            print(f"Błąd gniazda: {e}")
        finally:
            self.server_socket.close()
            log_event("Serwer został zamknięty")

if __name__ == "__main__":
    server = Server('127.0.0.1', 2900)
    server.run()
