import socket
import threading
import random
import datetime

def log_event(message):
    with open("server_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

class ClientThread(threading.Thread):
    def __init__(self, connection, address, number):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address
        self.number = number

    def run(self):
        log_event(f"Połączono z klientem {self.address}")
        self.connection.sendall(b"Zgadnij liczbe od 1 do 100\n")
        while True:
            try:
                data = self.connection.recv(1024).decode().strip()
                if not data:
                    break

                try:
                    guess = int(data)
                except ValueError:
                    self.connection.sendall(b"Blad: Podaj liczbe.\n")
                    continue

                if guess < self.number:
                    self.connection.sendall(b"Liczba jest za mala.\n")
                elif guess > self.number:
                    self.connection.sendall(b"Liczba jest za duza.\n")
                else:
                    self.connection.sendall(b"Gratulacje! Odgadles liczbe.\n")
                    break
            except ConnectionResetError:
                break

        log_event(f"Zakończono połączenie z klientem {self.address}")
        self.connection.close()

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

                number = random.randint(1, 100)
                log_event(f"Wylosowana liczba: {number}")

                client_thread = ClientThread(connection, address, number)
                client_thread.start()
        except socket.error as e:
            log_event(f"Błąd gniazda: {e}")
            print(f"Błąd gniazda: {e}")
        finally:
            self.server_socket.close()
            log_event("Serwer został zamknięty")


server = Server('127.0.0.1', 2900)
server.run()
