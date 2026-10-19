user = "Tomek"  # str
wiek = 51  # int
liczba = 908789765453123  # int

wersja = 3.90001
print(type(wersja))  # <class 'float'> liczby zmiennoprzecinkowe

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomek, masz teraz 51 lat.
# %d - digit - liczba
# %s - str
# print("Witaj %s, masz teraz %d lat." % (wiek, user))
# TypeError: %d format: a real number is required, not str

# f-string
print(f"Witaj {user}, masz teraz {wiek} lat.")
# Witaj Tomek, masz teraz 51 lat.

# %i - int, %f - float
print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3)  # Używamy wersji Pythona 3.000000
print("Używamy wersji Pythona %.2f" % 3)  # Używamy wersji Pythona 3.00
print("Używamy wersji Pythona %.1f" % 3)  # Używamy wersji Pythona 3.0
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4 - zaokrągla
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4 - zaokrągla

x = 3.8769
print(f"%.2f" % x)  # 3.88
print(x)

y = round(x, 2)
print(y)  # 3.88

print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.90001
print(f"Używamy wersji Pythona {wersja:.2f}")  # Używamy wersji Pythona 3.90
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.9
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 4
# print(f"Używamy wersji Pythona {wersja:.f}")  # ValueError: Format specifier missing precision

print(f"{user:<10}")  # "Tomek   "
print(f"{user:>15}")  # "          Tomek"
print(f"{user:^15}")  # "     Tomek     "
print(f"{user:.^15}")  # ".....Tomek....."

print(liczba)  # 908789765453123
print(f"Nasza duża liczba: {liczba:,}")  # Nasza duża liczba: 908,789,765,453,123
print(f"Nasza duża liczba: {liczba:_}")  # Nasza duża liczba: 908_789_765_453_123
print(f"Nasza duża liczba: {liczba:_}".replace("_", " "))  # Nasza duża liczba: 908 789 765 453 123
print(f"Nasza duża liczba: {liczba:_}".replace("_", "."))  # Nasza duża liczba: 908.789.765.453.123

liczba = 15000000000
liczba = 15_000_000_000
print(liczba)
print(type(liczba))  # <class 'int'>
