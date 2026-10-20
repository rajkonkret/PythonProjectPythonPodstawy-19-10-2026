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
