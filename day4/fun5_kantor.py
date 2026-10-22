# stworzyc funkcję kantor
# stworzyc dwie wew funkcje: eur, usd
# w zależności od parametru (kantor) zwrócic jedną z tych funcji (adres) (if)
# przekazanie kwoty do funkcji usd, eur

def kantor(waluta):
    print("Otwieram kantor")

    def usd(kwota=0):
        print(f"Wymieniam {kwota} usd na {kwota * 3.88}")

    def eur(kwota=0):
        print(f"Wymieniam {kwota} eur na {kwota * 4.35}")

    if waluta == "eur":
        return eur  # zwracamy adres funkcji, referencje
    else:
        return usd


kantor_usd = kantor("usd")
kantor_eur = kantor("eur")

kantor_eur(1000)
kantor_eur(1000)
kantor_eur(1000)
kantor_eur(1000)
kantor_eur(1000)

kantor_usd(500)
kantor_usd(500)
kantor_usd(500)
kantor_usd(500)
kantor_usd(500)
# Wymieniam 1000 eur na 4350.0
# Wymieniam 500 usd na 1940.0
