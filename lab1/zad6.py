import socket

def polacz_z_serwerem(adres, port):
    try:
        with socket.create_connection((adres, port)) as sock:
            print("Nawiązano połączenie z serwerem ")
    except socket.error as err:
        print(f"Nie udało się nawiązać połączenia z serwerem {err}")

adres_serwera = input("Podaj adres serwera: ")
port = int(input("Podaj numer portu: "))

polacz_z_serwerem(adres_serwera, port)
