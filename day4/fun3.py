a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne wewnątrz funkcji
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # działa na globalnych wartościach


def dodaj3():
    global a
    a = 7  # zmieniamy zawartośc globalnej a
    b = 90
    c = a + b
    print(a + b)


print(f"Zmienna a z góry(globalna) {a}")  # Zmienna a z góry(globalna) 10
dodaj()  # 15
print(f"Zmienna a z góry(globalna) {a}")  # Zmienna a z góry(globalna) 10
dodaj2()  # 20
print(f"Zmienna a z góry(globalna) {a}")  # Zmienna a z góry(globalna) 10
dodaj3()  # 97
print(f"Zmienna a z góry(globalna) {a}")  # Zmienna a z góry(globalna) 7
dodaj2()  # 17
# print(c)  # NameError: name 'c' is not defined
