# napisać kalkulator
# while True
# menu z opcjiami
# wyświetlić ładnie wynik -> f-string -> 5 * 8 = 40
# obsłużyc wyjątki

while True:
    print(f"""
1. Dodawanie
2. Odejmowanie
3. Mnożenie
4. Dzielenie
5. Koniec
""")

    odp = input("Wybierz opcję z menu: ")
    try:
        a = float(input("Podaj pierwsza liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

        if odp not in ['1', '2', '3', '4']:
            break

        if odp == "1":
            print(f"Dodawanie: {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Odejmowanie: {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Mnożenie: {a} * {b} = {a * b}")
        elif odp == "4":
            if b == 0:
                raise ZeroDivisionError("Nie dziel przez zero")
            print(f"Dzielenie: {a} / {b} = {a / b}")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except Exception as e:
        print("Błąd:", e)
    finally:
        print("Obliczenia wykonane")
