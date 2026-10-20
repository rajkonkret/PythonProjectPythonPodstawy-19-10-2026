# instrukcje warunkowe
# instrukcje sterowania przepływem programu

# if
# w zależnosci od warunku wykona jedna lub druga czesc progarmu (blok programu)
# wyrażenie w warunku musi zwrócić bool

odp = True

if odp: print('test')
# test

if odp:
    # blok programu wykonywany gdy warunek True
    print("Test")  # Test

# debugger - narzędzie do wykonywania programu krok po krok
# pułapka - miejsce zatrzymania programu
odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print()

odp = "Radek"

if odp:
    print("Działa")
# Działa

if odp == "Radek":
    print("Jestem Radek")
else:
    print("To nie Radek")
# Jestem Radek

odp = "Tomek"
if odp == "Radek":
    print("Jestem Radek")
elif odp == "Tomek":
    print("Jestem Tomek")
else:
    print("To nie Radek")
# Jestem Tomek

odp = 0
if odp:
    print("True")
else:
    print("False")  # False

# pobieramy od uzytkownika liczbę od 0 do 100
# jesli wynik wynosi 90 i więcej -> Bardzo dobry wynik
# jesli od 60 do 89 -> Egzamin zdany
# w przeciwnym razie -> Egzamin niezdany

# punkty = int(input("Podaj liczbę punktów: "))
#
# if punkty >= 90:
#     print("Bardzo dobry wynik")
# elif punkty >= 60:
#     print("Egzamin zdany")
# else:
#     print("Egzamin niezdany")
# # Podaj liczbę punktów: 60
# # Egzamin zdany

a = "Radek"
# jezeli długośc tekstu większa niz 3 wypisac:
# "Długość wynosi: ..., wiecej niż 3."

if len(a) > 3:
    print(f"Długość wynosi: {len(a)}, wiecej niż 3.")
# Długość wynosi: 5, wiecej niż 3.

n = len(a)
if n > 3:
    print(f"Długość wynosi: {n}, wiecej niż 3.")
# Długość wynosi: 5, wiecej niż 3.

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długość wynosi: {n}, wiecej niż 3.")
# Długość wynosi: 5, wiecej niż 3.

# pobrac zarobki
# jesli zarobki mniejsze od 10000 zł podatek 0%
# dla pozostałych podatek 90%
# wypisac obliczony podatek

# dodac podatek 0.2 dla przedziału 10000 do 39999
# dodc podatek 0.4 dla przedziału 40000 do 99999

zarobki = int(input("Podaj zarobki: "))

if zarobki < 10_000:
    podatek = 0
else:
    podatek = 0.9

print(f"Podatek wynosi: {zarobki * podatek} pln.")
