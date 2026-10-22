# klasa - przepis, szablon
# cechy (zmienne)
# metody (funkcje)
# obiekt - instancja klasy
# klasa musi zostac najpierw zadeklarowana
# tworzenie obiektu klasy uruchamia metodę inicjalizującą (konstruktor) __init__
# __del__ - destruktor
# paradygmaty -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase, UpperCamelCase
class Human:
    # pass
    """Klasa Human opisująca człowieka w pythonie"""

    imie = ""
    wiek = None
    plec = "k"


cz1 = Human()
print(cz1)
# <__main__.Human object at 0x000001BBC7ED7230>
print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
# print(print.__doc__)
# cd ..  - wyjście z katalogu
# cd day4 - wejscie do katalogu day4
# pydoc -b - serwer dokumentacji
# pydoc -w kl1 - plik html z dokumentacją

print(cz1.wiek)
print(cz1.imie)
print(cz1.plec)

cz1.imie = "Radek"
cz1.wiek = 55
cz1.plec = "m"

print(cz1.wiek)  # 55
print(cz1.imie)  # Radek
print(cz1.plec)  # m

cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 35

print(cz2.wiek)
print(cz2.imie)
print(cz2.plec)
# 35
# Anna
# k
