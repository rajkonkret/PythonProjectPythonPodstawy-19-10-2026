dictionary = {"imie": "Radek", 'nazwisko': "Kowalski"}

# klucz, wartośc, pary

# wypisze klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)

# imie
# nazwisko

# wartości
for i in dictionary.values():
    print(i)
# Radek
# Kowalski

# pary
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "<==>", v)
# imie <==> Radek
# nazwisko <==> Kowalski

# sep
# string inserted between values, default a space.
# end
# string appended after the last value, default a newline.

for k, v in dictionary.items():
    print(k, v, sep="<==>")
# imie<==>Radek
# nazwisko<==>Kowalski

for k, v in dictionary.items():
    print(k, v, sep="<==>", end=" | ")
    # imie<==>Radek | nazwisko<==>Kowalski |

print("Radek")  # imie<==>Radek | nazwisko<==>Kowalski | Radek
print("Nowa linia")
# imie<==>Radek | nazwisko<==>Kowalski | Radek
# Nowa linia
