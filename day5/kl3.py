from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa Ptak opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca - konstruktor
        :param gatunek:
        :param szybkosc:
        """

        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością:", self.szybkosc, "km/h")

    # metoda abstarakcyjna
    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa Kura, dziedziczy po klasie Ptak
    """

    def __init__(self, gatunek):
        # musimy wywołać super()
        # super() - klasa nadrzędna
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("Ko ko koko ko")


class Orzel(Ptak):
    """
    Klasa Orzel dziedziczy po klasie Ptak
    """

    def wydaj_odglos(self):
        print("Kier kiir kier kir kir")


# TypeError: Can't instantiate abstract class Sowa
# without an implementation for abstract method 'wydaj_odglos'
class Sowa(Ptak):
    """
    Klasa Sowa
    """


# TypeError: Can't instantiate abstract class Ptak
# without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 50)
# print(or1)
# or1.latam()
# # Tu Orzeł Lecę z szybkością: 50 km/h
#
# kur1 = Ptak("Kura", 0)
# print(kur1)
# kur1.latam()
# # Tu Kura Lecę z szybkością: 0 km/h

kur2 = Kura("Kura zielononóżka")
print(kur2)
kur2.latam()
# Tu Kura zielononóżka Ja nie latam.

or2 = Orzel("Bielik", 55)
print(or2)
or2.latam()
# Tu Bielik Lecę z szybkością: 55 km/h

kur2.wydaj_odglos()
or2.wydaj_odglos()
# Ko ko koko ko
# Kier kiir kier kir kir

# TypeError: Can't instantiate abstract class Sowa
# without an implementation for abstract method 'wydaj_odglos'
# sowa = Sowa("Sowa", 15)

# polimorfizm - obiekty róznych klas mają wspólne metody
lista = [or2, kur2]
for i in lista:
    i.wydaj_odglos()
#
# Kier kiir kier kir kir
# Ko ko koko ko
