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
