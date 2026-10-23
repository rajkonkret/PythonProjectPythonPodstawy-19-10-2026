# hermetyzacja

class Car:
    """
    Klasa opisująca samochód
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizująca - konstruktor
        :param model:
        :param year:
        """

        self.model = model
        self.year = year

        # pole prywatne
        # name mangling
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi: {self.__predkosc} km/h")

    def hamuj(self):
        if self.__predkosc > 0:
            self.__predkosc -= 10
            self.__zmiana_biegu()

    def __zmiana_biegu(self):
        print("Zmiana biegu")


car = Car("Mustang", 2026)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car.__predkosc)  # 50
car.licznik()  # Prędkość wynosi: 50 km/h
car.__predkosc = 0
car.licznik()  # Prędkość wynosi: 50 km/h
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()  # Prędkość wynosi: 0 km/h
# AttributeError: 'Car' object has no attribute '__zmiana_biegu'. Did you mean: '_Car__zmiana_biegu'?
# car.__zmiana_biegu()

# Prędkość wynosi: 50 km/h
# Prędkość wynosi: 50 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi: 0 km/h
