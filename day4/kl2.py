class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param wiek:
        :param imie:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się: {self.imie}")
        # self - przechowuje obiekt

    # wypiz_wiek(), wypisz_wzrost()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def ruszaj(self):

        if self.plec == "m":
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłam w drogę")

    # dopisac __str__
    def __str__(self) -> str:
        return f"{self.imie=} {self.wiek=} {self.plec=} {self.wzrost=}"


# cz1 = Human() # TypeError: Human.__init__() missing 3 required positional arguments: 'wiek', 'imie', and 'wzrost'
cz1 = Human("Radek", 45, 190, "m")
print(cz1)  # self.imie='Radek' self.wiek=45 self.plec='m' self.wzrost=190

cz1.powitanie()  # Nazywam się: Radek
cz1.wypisz_wiek()
cz1.wypisz_wzrost()
# Mam 45 lat.
# Mam 190 cm wzrostu.

cz2 = Human("Anna", 40, 167)
print(cz2)
# self.imie='Anna' self.wiek=40 self.plec='k' self.wzrost=167

cz2.powitanie()
cz2.wypisz_wzrost()
cz2.wypisz_wiek()
# Nazywam się: Anna
# Mam 167 cm wzrostu.
# Mam 40 lat.

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłem w drogę
# Ruszyłam w drogę
