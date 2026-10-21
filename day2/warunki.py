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

# zarobki = int(input("Podaj zarobki: "))
#
# # kolejność warunków ma znaczenie
# # jeden spełniony -> wyjście z ifa
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi: {zarobki * podatek} pln.")

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi: {rabat}")
# Rabat wynosi: 25

# operator warunkowy
rabat = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi: {rabat}")
# Rabat wynosi: 25

# napisac test z...
# trzy pytania
# punktacja za prawidłową odpowiedź

# punkty = 0
#
# odp = input("Podaj imię trenera: ")
# if odp.strip().casefold() == "Radek".casefold():
#     print('Opowiedź prawidłowa')
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Śpisz?!!!")
#
# odp = input("Która drużyna wygrała Mundial 2026: ")
# if odp.strip().casefold() == "Hiszpania".casefold():
#     print('Opowiedź prawidłowa')
#     punkty += 1
# else:
#     print('Sprawdz w internecie')
#
# odp = input("Jaki Król jest na banknocie 200 zł: ")
# if odp.strip().casefold() == "Zygmunt".casefold():
#     print('Opowiedź prawidłowa')
#     punkty += 1
# else:
#     print("Zerknij do portfela.")
#
# print("Punkty:", punkty)

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

# Podaj imię trenera: Radek
# Opowiedź prawidłowa
# Która drużyna wygrała Mundial 2026: Hiszpania
# Opowiedź prawidłowa
# Jaki Król jest na banknocie 200 zł: Zygmunt
# Opowiedź prawidłowa
# Punkty: 3


# zasymulejmy system zbierania logów
# zmienna: typ_sytemu -> console, email, inny
# console: "Stało się coś strasznego!"
# email: "System email"
# -----
# jesli system jest 'email' to:
# do listy błedów dopisać tłumaczenie błedu
# error_level -> error, medium, inny
# error -> Krytyczny

typ_systemu = 'email'
error_level = "medium"
lista_b = []

if typ_systemu == "console":
    print("Stało się coś strasznego")

elif typ_systemu == 'email':
    print("System email")
    if error_level == "error":
        lista_b.append("Krytyczny")
    elif error_level == "medium":
        lista_b.append("Ostrzeżenia")
    else:
        lista_b.append("inny")
else:
    print("Inny system")

print(lista_b)
# ['Ostrzeżenia']
