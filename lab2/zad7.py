import socket

def polacz_z_serwerem(adres, port):
    try:
        with socket.create_connection((adres, port)) as sock:
            print(f"Nawiązano połączenie z serwerem na porcie {port}")
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown service"
            print(f"Usługa uruchomiona na porcie {port}: {service}")
    except socket.error as err:
        print(f"Nie udało się nawiązać połączenia z serwerem: {err}")
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown service"
        print(f"Port {port} jest zamknięty lub nieosiągalny - możliwa usługa: {service}")

adres_serwera = input("Podaj adres serwera: ")
port = int(input("Podaj numer portu: "))

polacz_z_serwerem(adres_serwera, port)

