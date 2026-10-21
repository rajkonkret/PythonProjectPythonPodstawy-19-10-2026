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
