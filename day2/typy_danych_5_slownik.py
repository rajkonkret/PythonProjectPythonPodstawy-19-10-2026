# słownik - para {klucz : wartosc}
# {'user' : 'Radek'}
# klucze nie mogą sie powtarzac
# słownik jest odpowiednikiem jsona

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dict_1 = dict()
print(dict_1)  # {}
print(type(dict_1))  # <class 'dict'>

# dodawanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}

# dodac klucz wiek
dictionary['wiek'] = 54
print(dictionary)  # {'imie': 'Radek', 'wiek': 54}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 54])
# dict_items([('imie', 'Radek'), ('wiek', 54)])

# nadpisanie wartości
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 54}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek

dictionary['imie'] = ["Radek", "Tomek", "Anna"]
print(dictionary)  # {'imie': ['Radek', 'Tomek', 'Anna'], 'wiek': 54}

# wypisac Tomek
print(dictionary['imie'])  # ['Radek', 'Tomek', 'Anna']
print(dictionary['imie'][1])  # Tomek

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary['Imie'.lower()])  # ['Radek', 'Tomek', 'Anna']

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

print(chr(223))  # ß
# \xhh szesnatkowy kod znaku
print("\u00DF")  # ß
# \N{name}
print("\N{LATIN SMALL LETTER SHARP S}")  # ß

name1 = "GROSS"
name2 = "groß"

print(name1 == name2)  # False
print(name1.lower() == name2.lower())  # False
# Return a version of the string suitable for caseless comparisons.
print(name1.casefold() == name2.casefold())  # True

dictionary.update({'data': '12-12-2067'})
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Anna'], 'wiek': 54, 'data': '12-12-2067'}

# [('imie', 'Radek'), ('wiek', 54)]
dict_small = {'x': 20}
dict_small.update([('y', 3), ("z", 78)])
print(dict_small)  # {'x': 20, 'y': 3, 'z': 78}

# input() - możliwosć wprowadzenia danych do komputera np.:  z klawiatury

tekst = input("Podaj imię: ")
print(tekst)
# Podaj imię: Radek
# Radek
