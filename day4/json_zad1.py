# {
#   "name": "John",
#   "age": 30,
#   "city": null
# }
# json - dane typu klucz - wartosc
#  typ wymiany pomiędzy klient serwer
# odpowiednikiem jsona w pythonie jest słownik
# zawsze podwójne cudzysłowia
# None -> null
lista = ["Radek"]
print(lista)  # ['Radek']

# orjson
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>
print(person_dict)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}

# zapis danych jako json
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

# beautify
with open('nasze_dane_b.json', "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# sortowaanie po kluczach
with open('nasze_dane_sorted.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', "r") as file:
    data = json.load(file)

print(data)
# {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(data))
# <class 'dict'>
