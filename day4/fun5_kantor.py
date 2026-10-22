# stworzyc funkcję kantor
# stworzyc dwie wew funkcje: eur, usd
# w zależności od parametru (kantor) zwrócic jedną z tych funcji (adres) (if)
# przekazanie kwoty do funkcji usd, eur

def kantor(waluta):
    print("Otwieram kantor")

    def usd():
        print("Wymieniam usd")

    def eur():
        print("Wymieniam eur")

    if waluta == "eur":
        return eur
    else:
        return usd
