wiek = 47  # int
rok = 2026  # int
temp = 36.6  # float
temp2 = 36, 6
print(type(temp2))  # <class 'tuple'>

print(wiek + rok)  # 2073
print(wiek - rok)  # -1979
print(wiek * rok)  # 95222
print(wiek / rok)  # 0.02319842053307009 -> float
print(rok / wiek)  # 43.1063829787234
print(rok // wiek)  # 43 - częśc całkowita z dzielenia

print(2026 - 43 * 47)  # 5 reszta z dzielenia
print(rok % wiek)  # modulo, reszta z dzielenia, 5

print(10 % 3)  # reszta 1

print(wiek ** rok)  # potęgowanie
print(len(str(wiek ** rok)))  # potęgowanie, długosc 3388
print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit