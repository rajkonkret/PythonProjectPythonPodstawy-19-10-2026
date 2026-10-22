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


cz1 = Human()
print(cz1)
# <__main__.Human object at 0x000001BBC7ED7230>
print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
# print(print.__doc__)
# cd ..  - wyjście z katalogu
# cd day4 - wejscie do katalogu day4
# pydoc -b - serwer dokumentacji
# pydoc -w kl1 - plik html z dokumentacją
