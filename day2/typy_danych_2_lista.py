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
