import sys

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
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# błąd zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.3)  # 0.4
print(0.1 + 0.2)  # 0.30000000000000004

# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308,
# min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# decimal() - pozwala ominąc problem zaokrąglenia

# typ logiczny
# prawda, fałsz
# True, False
# 1, 0

czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, boolean, typ logiczy

print(int(True))  # 1
print(int(False))  # 0

# bool() rzutowanie na typ logiczny
print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-100))  # True

print(bool("Radek"))  # True

print(bool(""))  # False

print(bool("0"))  # True

print(None)  # odpowiednik null, stan nieokreslony, nie wiem
print(bool(None))  # False

# operacje logiczne
print(40 * "-")

# and - i
print(False and True)
print(False and False)
print(True and False)
print(True and True)
# ----------------------------------------
# False
# False
# False
# True

print(35 * "-")

# or - lub
print(False or True)
print(False or False)
print(True or False)
print(True or True)
# -----------------------------------
# True
# False
# True
# True

print(30 * "-")

# not - negacja
print(not True)
print(not False)
# ------------------------------
# False
# True

a = 6
b = 9

print(f"Porownanie {a} > {b} = {a > b}")  # Porownanie 6 > 9 = False
print(f"Porownanie {a} < {b} = {a < b}")  # Porownanie 6 < 9 = True
print(f"Porownanie {a} >= {b} = {a >= b}")  # Porownanie 6 >= 9 = False
print(f"Porownanie {a} <= {b} = {a <= b}")  # Porownanie 6 <= 9 = True

print(f"Porównanie {a <= b = }")  # Porównanie a <= b = True

print(f"Porównanie {a} == {b} = {a == b}")  # czy są równe: Porównanie 6 == 9 = False
print(f"Porównanie {a} != {b} = {a != b}")  # czy są różne!!!: Porównanie 6 != 9 = True
