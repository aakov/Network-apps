import shutil

nazwa_wejsciowego = input("Podaj nazwę pliku : ")
nazwa_wyjsciowego = "lab1zad1.png"

try:
    shutil.copyfile(nazwa_wejsciowego, nazwa_wyjsciowego)
    print("Plik skopiowany ")
except FileNotFoundError:
    print("Nie znaleziono pliku ")