nazwa_wejsciowego = input("Podaj nazwę pliku :")
nazwa_wyjsciowego = "lab1zad1.txt"
with open(nazwa_wejsciowego, 'r') as plik_wejsciowy:
    with open(nazwa_wyjsciowego, 'w') as plik_wyjsciowy:
        for i in plik_wejsciowy:
            plik_wyjsciowy.write(i)
print("Skopiowano ")

