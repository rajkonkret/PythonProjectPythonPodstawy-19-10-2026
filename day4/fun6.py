# napisac funkcję obliczającą średnią ocen
# ma dziłać z dowolną liczbą argumentów
# ma obsłużyć błedy
# statistics - funkcje statystyczne np.: średnia, mediana
# dodac imię ucznia
import statistics


def srednia(name=None, *cyfry):  # dowolna ilosc elementów przekazanych po pozycji
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
        print(f"Srednia dla ucznia {name} wynosi: {avg}")  # Srednia dla ucznia Radek wynosi: 7.0
        print(f"Srednia dla ucznia {name} wynosi: {avg_p}")  # Srednia dla ucznia Radek wynosi: 7.0
        print(f"Srednia dla ucznia {name} wynosi: {statistics.mean(cyfry)}")  # Srednia dla ucznia Radek wynosi: 7
    finally:
        print("Nasstępny uczeń")


srednia()  # ()
srednia(1)  # (1,)
srednia(11, 2)  # (11, 2)
srednia("Radek", 7, 7, 7, 7, 6, 7, 8)
