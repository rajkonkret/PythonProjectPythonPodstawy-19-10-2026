# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

# csv - dane oddzielone znakiem podziału -> ,;tab|

import csv

row = ['radek', 'coe', "3", 0]
columns = ['name', 'branch', 'year', 'cgpa']

filename = 'records.csv'

# newline=""
with open(filename, "w", newline="") as csv_f:
    csv_writer = csv.writer(csv_f)

    csv_writer.writerow(columns)  # zapis wiersza
    csv_writer.writerow(row)  # zapis wiersza

dict_name = dict(zip(columns, row))
print(dict_name)
print(type(dict_name))
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': 0}
# <class 'dict'>

filename = "records_dict.csv"

with open(filename, "w", newline="") as csv_f:
    # csv_writer = csv.DictWriter(csv_f, fieldnames=columns)
    csv_writer = csv.DictWriter(csv_f, fieldnames=dict_name.keys())
    csv_writer.writeheader()  # nagłówki
    csv_writer.writerow(dict_name)

products = [
    {"sku": 1, 'exp_date': 'today', "price": 200},
    {"sku": 2, 'exp_date': 'today', "price": 300},
    {"sku": 3, 'exp_date': 'tomorrow', "price": 400},
    {"sku": 4, 'exp_date': 'today', "price": 1200},
    {"sku": 5, 'exp_date': 'today', "price": 900},
    {"sku": 6, 'exp_date': 'tomorrow', "price": 200.99},
    {"sku": 7, 'exp_date': 'today', "price": 100},
]
