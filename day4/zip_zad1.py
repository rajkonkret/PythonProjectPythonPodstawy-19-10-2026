import time
from itertools import zip_longest

imiona = ["Ala", "Zenek", "Tomek", "Basia", "Radek"]
wiek = [24, 18, 34, 20]

zipped = zip_longest(imiona, wiek, fillvalue="Brak")
print(zipped)  # <itertools.zip_longest object at 0x0000023DA252C900>

# for i in zipped:
#     print(i)

# ('Ala', 24)
# ('Zenek', 18)
# ('Tomek', 34)
# ('Basia', 20)
# ('Radek', 'Brak')

print(50 * "-")
lista = []
for o, w in zipped:
    print(o, w)
    time.sleep(1)
    lista.append(o)

print(lista)
# ['Ala', 'Zenek', 'Tomek', 'Basia', 'Radek']
