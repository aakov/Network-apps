import socket

server_address = '212.182.24.27'
server_port = 2912

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_address, server_port))

while True:
    number = input("Podaj liczbę do odgadnięcia: ")
    if not number.isdigit():
        print("Źle ")
        continue

    try:
        sock.sendall(number.encode())
        response = sock.recv(1024).decode()
        print(f"Odpowiedź serwera: {response}")

        if response == "Odgadłeś ":
            print("Odgadłeś liczbę ")
            break
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        break

sock.close()
