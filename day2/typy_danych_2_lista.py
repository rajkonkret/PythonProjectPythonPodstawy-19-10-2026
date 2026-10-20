# kolekcje

# lista - zachowuje kolejnosc, pozwala przechowywac dowolną ilośc danych, różnego typu na raz

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# dodawanie elemntów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Klaudia")
lista.append("Anna")
lista.append("Darek")
lista.append("Kasia")
print(lista)  # ['Radek', 'Tomek', 'Klaudia', 'Anna', 'Darek', 'Kasia']

# długosc listy
print(len(lista))  # długośc 6

# ['Radek', 'Tomek', 'Klaudia', 'Anna', 'Darek', 'Kasia']
#     0        1         2         3       4        5

print(lista[2])  # Klaudia
print(lista[4])  # Darek

# print(lista[10])  # IndexError: list index out of range

print(lista[5])
print(lista[len(lista) - 1])  # Kasia
print(lista[-1])  # Kasia

print(lista[-2])

# ['Radek', 'Tomek', 'Klaudia', 'Anna', 'Darek', 'Kasia']
#     0        1         2         3       4        5
#     -6       -5        -4        -3      -2       -1

# slicowanie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Klaudia'] -> indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Klaudia']

print(lista[2:])  # ['Klaudia', 'Anna', 'Darek', 'Kasia'] włacznie z ostatnim
print(lista[2:5])  # ['Klaudia', 'Anna', 'Darek'] bez ostatniego

print(lista[2:10])  # ['Klaudia', 'Anna', 'Darek', 'Kasia']

print(lista[15:20])  # [] - pusta lista

print(lista[:])  # ['Radek', 'Tomek', 'Klaudia', 'Anna', 'Darek', 'Kasia']

# ['Radek', 'Tomek', 'Klaudia', 'Anna', 'Darek', 'Kasia']
#     0        1         2         3       4        5
#     -6       -5        -4        -3      -2       -1

print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Klaudia', 'Anna']

a = None
b = None
print(lista[a:b])  # ['Radek', 'Tomek', 'Klaudia', 'Anna', 'Darek', 'Kasia']

# wygenerowac liste z zakresu 0 do 14
# lista_15  =[0,1,2...]
lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[::2])  # [0, 2, 4, 6, 8, 10, 12, 14], [start:stop:krok]
print(lista_15[::3])  # [0, 3, 6, 9, 12]

print(lista_15[::-1])  # odwrotna kolejność
# [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(list(range(5, 15, 2)))  # [5, 7, 9, 11, 13] (start, stop, krok)

lista1 = [1, 2, 3]
lista2 = [7, 8, 9]
print(lista1 + lista2)  # [1, 2, 3, 7, 8, 9]

lista1.append(list(range(5, 9)))  # jako lista w liscie
print(lista1)  # [1, 2, 3, [5, 6, 7, 8]]
lista2.extend(list(range(5, 9)))  # jako kolejne elementy listy
print(lista2)  # [7, 8, 9, 5, 6, 7, 8]

# python nie ma typu danych tablica (array)
tablica = [[1, 2], [3, 4]]
print(tablica)
# numpy - biblioteka do pracy z tablicami/macierzami

print(lista)
# ['Radek', 'Tomek', 'Klaudia', 'Anna', 'Darek', 'Kasia']

# nadpisanie na wskazanym indeksie
lista[2] = "Alicja"
print(lista)  # ['Radek', 'Tomek', 'Alicja', 'Anna', 'Darek', 'Kasia']

# dopisanie elementu we wskazanym miejscu (indeksie)
lista.insert(1, "Ola")
print(lista)
# ['Radek', 'Ola', 'Tomek', 'Alicja', 'Anna', 'Darek', 'Kasia']

# sprawdzenie indeksu
print(lista.index("Darek"))  # 5

# dopiszcie do listy taki elementy jak juz jest
lista.append("Tomek")
print(lista)
print(lista.index("Tomek"))
# ['Radek', 'Ola', 'Tomek', 'Alicja', 'Anna', 'Darek', 'Kasia', 'Tomek']
# 2

# usnięcie elemntu z listy, pierwszy napotkany od lewej
lista.remove("Tomek")
print(lista)
# ['Radek', 'Ola', 'Alicja', 'Anna', 'Darek', 'Kasia', 'Tomek']

# usunięcie po indeksie, zwraca usunięty element
# pop()
print(lista.pop(2))  # Alicja
print(lista)  # ['Radek', 'Ola', 'Anna', 'Darek', 'Kasia', 'Tomek']

zmienna = lista.pop()  # usunie ostatni element
print(zmienna)  # Tomek

# typy proste
a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3

b = 9
print(f"{a=}, {b=}")  # a=3, b=9

# kolekcje
lista2 = lista  # kopia referencji, adresu
print(lista)  # ['Radek', 'Ola', 'Anna', 'Darek', 'Kasia']
print(lista2)  # ['Radek', 'Ola', 'Anna', 'Darek', 'Kasia']

lista_copy = lista.copy()  # kopia listy w nowym miejscu

lista.clear()  # usuniecie wszystkich eleemntów z listy
print(lista)  # []
print(lista2)  # []
print(lista_copy)  # ['Radek', 'Ola', 'Anna', 'Darek', 'Kasia']

# id()
print(id(lista))  # 2231366578240
print(id(lista2))  # 2231366578240
print(id(lista_copy))  # 2231368821248

liczby = [54, 999, 12.34, 34, 567, 999]
print(type(liczby))  # <class 'list'>

# wypisac liczby
# nadpisac czwart element inną liczbą
# wyciągnąć elementy od pierwszego do trzeciego włącznie
# wypisac po indeksie dodtanim i ujemnym
