# wyjatki - błędy wykonywanie programy

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPythonPodstawy-19-10-2026\day3\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1

lista = []
# obsługa wyjątków
try:
    # print(5 / 0)
    # lista[1]
    # int("Q")
    # print(2 + "Ania")

    # raise KeyError("Bład klucza")  # rzuci błąd
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except IndexError:
    print("Brak elementu w liście")
except ValueError:
    print("Bład wartości")
except TypeError:
    print("Bład typu")
except Exception as e:
    print("Bład:", e)
else:  # tylko gdy nie ma błedu
    print(wynik)
finally: # wykonuje się zawsze
    print("Następna osoba")

print("Dalsza częśc programu")
# Nie dziel przez zero
# Dalsza częśc programy
#
# Process finished with exit code 0
# Bład: 'Bład klucza'
# Dalsza częśc programy
