# funkcje zwracające wynik
# kończy się słowkiem return

a = 9
b = 98


def dodaj():
    return a + b  # zwróc wynik dodawania


# funkcja odejmij, z trzema argumentami domyślnymi
def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj())  # 107

wynik = dodaj()
print("Wynik:", wynik)

print(odejmij())
print(odejmij(1))
print(odejmij(1, 2))
print(odejmij(1, 2, 3))
print(odejmij(c=1, a=2, b=3))
print(odejmij(1, c=9))  # -8


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(oblicz_vat(1000))
print(oblicz_vat(vat=9, kwota=1000))
# 1230.0
# 1090.0

zm = oblicz_vat(1000)
if zm == 1230:
    print("Ok")

print(dodaj() + odejmij(1, 6, 9))  # 93
