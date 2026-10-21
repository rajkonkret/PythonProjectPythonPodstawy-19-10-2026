# pętla - możliwośc wykonania kodu wielokrotnie
# for - pętla iteracyjna

for i in range(5):  # od 0 do 4
    print(i)

for i in range(20):
    pass  # nic nie rób

print(i)  # 19

for i in range(5, 10):  # od 5 do 9
    print(i)
# 5
# 6
# 7
# 8
# 9

for _ in range(10):  # niema zmienna
    print("Test podłoga")
    print(_)  # 9

for i in range(5):
    print(i * 2)
    print(i + 2)

print("Wyjście z pętli")

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta


# lotto jako pętla
# wyniki do listy
import random

listy_wyl = []

# lista_kul = list(range(1, 50))
# print(lista_kul)
# 10 lsowań

for losowanie in range(0, 10):
    lista_kul = list(range(1, 50))
    listy_wyl = []
    for _ in range(6):
        kula = random.choice(lista_kul)
        lista_kul.remove(kula)
        # print(kula)  # 10
        listy_wyl.append(kula)

    # print(listy_wyl)
    print(losowanie, listy_wyl)
# [9, 19, 41, 36, 4, 26]

# parzyste do listy 0 9

lista3 = []
for i in range(10):
    if i % 2 == 0:
        lista3.append(i)

print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

# wypisac elementy z listy za pomoca for
# indeksy elementów
for i in range(len(lista3)):
    print(f"wartośc: {lista3[i]}")

for c in lista3:  # pod c podstawia kolejne elementy listy
    print(c)

lista_nazwy = ["Ala", "Tomek", "Zenek", "Basia"]

for p in lista_nazwy:
    print(p)
# Tomek
# Zenek
# Basia

for i in range(len(lista_nazwy)):
    print(f"index: {i}, wartośc: {lista_nazwy[i]}")
# index: 0, wartośc: Ala
# index: 1, wartośc: Tomek
# index: 2, wartośc: Zenek
# index: 3, wartośc: Basia

for i in lista_nazwy:
    print(lista_nazwy.index(i), i)
# 0 Ala
# 1 Tomek
# 2 Zenek
# 3 Basia

# enumerate() - zwraca/nadaje numer i element kolekcji
for p in enumerate(lista_nazwy):
    print(p)
# (0, 'Ala')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Basia') -> 3 Basia

a, b = (3, 'Basia')
print(a, b)

for i, o in enumerate(lista_nazwy):
    print(i, o)
# 0 Ala
# 1 Tomek
# 2 Zenek
# 3 Basia

for i, o in enumerate(lista_nazwy, start=1):
    print(i, o)
# 1 Ala
# 2 Tomek
# 3 Zenek
# 4 Basia

print(lista3)

for c in lista3:
    if c > 4:
        print(c, "Większe niż 4")
    elif c == 4:
        print(c, "Równa 4")
    else:
        print(c, "Mniejsze niż 4")
    print(c, "Za każdym przejsciem pętli")
print("Po zakończeniu pętli")
# 0 Mniejsze niż 4
# 0 Za każdym przejsciem pętli
# 2 Mniejsze niż 4
# 2 Za każdym przejsciem pętli
# 4 Równa 4
# 4 Za każdym przejsciem pętli
# 6 Większe niż 4
# 6 Za każdym przejsciem pętli
# 8 Większe niż 4
# 8 Za każdym przejsciem pętli
# Po zakończeniu pętli
