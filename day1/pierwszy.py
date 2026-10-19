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

# zmienna - pudełko, szufladka na dane

name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

age = 89
print(age)  # 89
print(type(age))  # <class 'int'>

# typowanie dynamiczne
age = 'Radek'
print(age)  # Radek
print(type(age))  # <class 'str'>

age = "90"
# print(age + 10)  # TypeError: can only concatenate str (not "int") to str

print(age * 2)  # 9090

# podpowiedzi typów
name: str = "Radek"
print(name)
print(type(name))

name = 90
print(name)  # 90

# mypy, pyright, ruff
# pip - menadżer pakietów
# pip install mypy
# cd .\day1\ - zmmiana katalogu
# mypy .\pierwszy.py
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProjectPythonPodstawy-19-10-2026\day1> mypy .\pierwszy.py
# pierwszy.py:61: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# pierwszy.py:65: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# pierwszy.py:71: error: Name "name" already defined on line 52  [no-redef]
# pierwszy.py:75: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 4 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProjectPythonPodstawy-19-10-2026\day1>
