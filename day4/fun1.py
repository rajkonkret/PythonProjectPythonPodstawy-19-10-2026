# funkcja - wydzielony fragment kodu, mozna wywołac w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# wywołanie funkcji uruchamia funkcję

a = 6
b = 8


# deklaracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):  # dwa obowiązkowe do przekazania argumenty
    print(a + b)


# ominięcie problemu braku przeiązania funkcji liczbą argumentów
def odejmij(a, b, c=0):  # argument o wartości domyślnej
    print(a - b - c)


# wywołanie funkcji
dodaj()  # 14

# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 89)  # 94

odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4
