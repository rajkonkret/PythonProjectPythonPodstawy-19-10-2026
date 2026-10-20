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

punkty = int(input("Podaj liczbę punktów: "))

if punkty >= 90:
    print("Bardzo dobry wynik")
elif punkty >= 60:
    print("Egzamin zdany")
else:
    print("Egzamin niezdany")
# Podaj liczbę punktów: 60
# Egzamin zdany
