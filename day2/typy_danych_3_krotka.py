# krotka (tupla) - kolekcja tylko do odczytu, niemutowalna
# pozwala efektywniej zarządzać pamiecią
# krotka jako stała - szczególny przypadek zmiennej

tupla_imiona = "Zenek", "Marek", "Radek", "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')

# tupla_liczby = (43, 55, 22.34, 11, 200)
tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)
print(type(tupla_liczby))  # <class 'tuple'>

# tupla jednoelementowa
tupla_jeden = (45,)  # PEP8 zaleca przy jednoelementowych tuplach nawiasy
tupla_jeden = 45,
print(type(tupla_jeden))  # <class 'tuple'>
print(tupla_jeden)  # (45,)

del tupla_jeden  # usunięcie calej tupli
# print(tupla_jeden)  # NameError: name 'tupla_jeden' is not defined

# tupla_liczby[0] = 123  # TypeError: 'tuple' object does not support item assignment

print(tupla_imiona)

print(tupla_imiona.index("Radek"))  # indeks 2
print(tupla_imiona.count("Radek"))  # występuje jeden raz

print(len(tupla_imiona))  # długość 4

tup = 1, 2
print(type(tup))  # <class 'tuple'>

# a - pierwszy, b - drugi

a = tup[0]
b = tup[1]
print(a, b)

# rozpakowanie tupli
c, d = tup
print(c, d)  # 1 2

# zamiana miejscami wartosci zmiennych
a, b = b, a
print(b, a)

print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')
# name1, name2, name3
# name1, name2, name3 = tupla_imiona  # ValueError: too many values to unpack (expected 3, got 4)
name1, name2, *name3 = tupla_imiona  # * worek na pozostałe dane, dowolna ilość danych
print(name1, name2, name3)  # Zenek Marek ['Radek', 'Ania']

*name1, name2, name3 = tupla_imiona  # * worek na pozostałe dane, dowolna ilość danych
print(name1, name2, name3)  # ['Zenek', 'Marek'] Radek Ania

name1, *name2, name3 = tupla_imiona  # * worek na pozostałe dane, dowolna ilość danych
print(name1, name2, name3)  # Zenek ['Marek', 'Radek'] Ania

# name1, name2, name3, name4, name5 = tupla_imiona # ValueError: not enough values to unpack (expected 5, got 4)
