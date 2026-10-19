print()  # wypisz/wydrukuj

print('Witaj Świecie')
print("Witaj Świecie")

# ctrl / - komentarz
# print('Radek")
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPythonPodstawy-19-10-2026\day1\pierwszy.py", line 6
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 6)
#
# Process finished with exit code 1 - program zakończył się z błędem

# ctrl d - powielanie linii
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")

# type() - sprawdzanie typu danych
print(type("Radek"))  # <class 'str'>, typ tekstowy

print("38" + "90")  # 3890 łączenie tekstów, konkatencja
print("Radek" + "1")  # Radek1

print(38 + 90)  # 128
print(type(90))  # <class 'int'> liczby całkowite

# sys
import sys

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

# print("29" + 89)  # TypeError: can only concatenate str (not "int") to str

# rzutowanie typów int(), str()
print(int("39") + int(30))  # 69
print("Radek" + str(1))  # Radek1

print(168 * "35")  # mnożenie tekstów
