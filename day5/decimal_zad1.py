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

kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem:", kwota_z_podatkiem)  # Kwota z podatkiem: 12.6075
print("Kwota z podatkiem:", kwota_z_podatkiem.quantize(precyzja))  # Kwota z podatkiem: 12.61
