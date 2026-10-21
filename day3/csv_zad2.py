import csv

# filename = "records.csv"
# filename = "records_discount.csv"
filename = "records_discount_semicolon.csv"

columns = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter) # ;
    print(dialect.quotechar) # "

    # StopIteration - skończyły się dane
    csv_f.seek(0)  # wracamy na początek pliku

    # csv_reader = csv.reader(csv_f, delimiter=";")
    csv_reader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csv_reader)
    # <_csv.reader object at 0x0000029EA0B185E0>

    columns = next(csv_reader)  # odczytaj daną linię i ustaw odczyt na następną

    for row in csv_reader:  # czyta od kolejnej lini tutaj od drugiej
        rows.append(row)

print("Columns:", columns)
print("Rows:", rows)
# Columns: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]
# Rows: [['1', 'today', '200'], ['2', 'today', '300'], ['3', 'tomorrow', '400'], ['4', 'today', '1200'],
# ['5', 'today', '900'], ['6', 'tomorrow', '200.99'], ['7', 'today', '100']]
# Rows: [['1;today;200'], ['2;today;300'], ['3;tomorrow;400'], ['4;today;1200'],
# ['5;today;900'], ['6;tomorrow;200.99'], ['7;today;100']]