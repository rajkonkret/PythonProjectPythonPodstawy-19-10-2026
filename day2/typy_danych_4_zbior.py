# zbior (set) - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# nie ma indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11, 777]
zbior = set(lista)  # rzutowanie na zbiór
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} zmiana kolejności

sortowanie = sorted(zbior)  # zwróćiło listę
print(sortowanie)  # [11, 22, 33, 44, 55, 66, 777]

# pusty zbiór
zb2 = set()  # tylko iwyłacznie słowkiem set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(24)
zbior.add(18)
zbior.add(25)
zbior.add(33)
zbior.add(33)
zbior.add(24)
zbior.add(33)
zbior.add(12)
zbior.add(33)
print(zbior)  # {33, 66, 777, 11, 44, 12, 18, 22, 55, 24, 25}

# usunięcie elemntu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 12, 18, 22, 24, 25}

# pop() - usunięcie pierwszego
print(zbior.pop())
print(zbior)  # {66, 777, 11, 44, 12, 18, 22, 24, 25}

zmienna = zbior.pop()
print(f"Zmienna: {zmienna}")  # Zmienna: 66
print("Zmienna:", zmienna)  # Zmienna: 66

zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(zbior_2)
print(type(zbior_2))
# {18, 667, 52, 11, 44, 12.34, 62}
# <class 'set'>

# operacje na zbiorach - zwraca nowy zbior
# suma zbiorów
print(zbior | zbior_2)  # {777, 11, 44, 12, 12.34, 18, 52, 22, 24, 25, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12, 12.34, 18, 52, 22, 24, 25, 667, 62}

# częśc wspólna zbiorów
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica zbiorów
print(zbior - zbior_2)  # {777, 12, 22, 24, 25}
print(zbior.difference(zbior_2))  # {777, 12, 22, 24, 25}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# zmienia bazowy
zbior.update(zbior_2)
print(zbior)  # {777, 11, 44, 12, 12.34, 18, 52, 22, 24, 25, 667, 62}

# zamiana zbioru na krotke i listy
krotka = tuple(zbior)
print(krotka)  # (777, 11, 44, 12, 12.34, 18, 52, 22, 24, 25, 667, 62)

lista = list(zbior)
print(lista)  # [777, 11, 44, 12, 12.34, 18, 52, 22, 24, 25, 667, 62]

# in
# spradzenie czy dany element istnieje w kolekcji

print(667 in lista)  # True
print(667 in krotka)  # True
print(667 in zbior)  # True
print(787 in zbior)  # False
