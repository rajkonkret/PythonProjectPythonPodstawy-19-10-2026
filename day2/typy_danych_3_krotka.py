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
