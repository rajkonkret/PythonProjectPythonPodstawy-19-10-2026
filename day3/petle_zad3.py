# while - petla sterowana warunkiem

# pętla nieskońćzona
# while True:
#     print("Komunikat")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)  # 11
print(50 * "-")

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")

# liczby = []
# liczby_int = []
# while True:
#
#     liczba = input("Wprowadz liczbę całkowitą:")  # str
#
#     if liczba.isnumeric():
#         liczby.append(liczba)
#         liczby_int.append(int(liczba))
#     else:
#         break

# print(liczby)
# print(liczby_int)
# Wprowadz liczbę całkowitą:1
# Wprowadz liczbę całkowitą:2
# Wprowadz liczbę całkowitą:3
# Wprowadz liczbę całkowitą:a
# ['1', '2', '3']

# Wprowadz liczbę całkowitą:1
# Wprowadz liczbę całkowitą:2
# Wprowadz liczbę całkowitą:3
# Wprowadz liczbę całkowitą:a
# ['1', '2', '3']
# [1, 2, 3]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
# usunac wszystkie wystąpienia liczby 5
while 5 in my_list:
    my_list.remove(5)
print(my_list)  # [1, 2, 3, 4, 6]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}

print(list(dict.fromkeys(my_list)))
# [1, 5, 2, 3, 4, 6] usunięte duplikaty bez zmiany kolejności
