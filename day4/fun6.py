# napisac funkcję obliczającą średnią ocen
# ma dziłać z dowolną liczbą argumentów
# ma obsłużyć błedy

def srednia(*cyfry):  # dowolna ilosc elementów przekazanych po pozycji
    print(cyfry)

    count = len(cyfry)

    suma = 0
    suma_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"Srednia wynosi: {avg}")
        print(f"Srednia wynosi: {avg_p}")
    finally:
        print("Nasstępny uczeń")


srednia()  # ()
srednia(1)  # (1,)
srednia(11, 2)  # (11, 2)
