import socket

adres = input("Podaj adres serwera: ")

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((adres, port))
        if result == 0:
            print(f"Port {port} jest otwarty.")
        sock.close()
except socket.gaierror:
    print(f"Nie można znaleźć adresu IP dla hosta {adres}")
except socket.error as err:
    print(f"Wystąpił błąd podczas połączenia z serwerem  {err}")

