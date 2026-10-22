# funkcja lambda
# skrócony zapis funkcji
# lambda zawsze zwraca wynik - return
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(6, 90))  # -84

odejmij2 = lambda a, b: a - b  # return
print(odejmij2(6, 90))  # -84

# przerobic na lambdę
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))  # 1230.0
