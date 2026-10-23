# decimal - omija problem zaokrąglenia

from decimal import Decimal

kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')
kwota3 = Decimal(3.0)

print(kwota1)
print(kwota2)
print(kwota3)
# 10.25
# 5.50
# 5.5

print(kwota1 + kwota2)  # 15.75
suma = kwota1 + kwota2
print("Suma:", suma)  # Suma: 15.75

precyzja = Decimal('0.00')

podatek = Decimal('0.23')

