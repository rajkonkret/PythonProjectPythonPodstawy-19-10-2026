import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

response = requests.get(url)
print(response)

data = response.json()  # zamiana na słownik
print(data)
print(type(data))

print("Waluta:", data['currency'])  # Waluta: dolar amerykański
print(data['rates'])
# [
# {'no': '207/A/NBP/2026', 'effectiveDate': '2026-10-23', 'mid': 3.9247}
# ]
print(data['rates'][0])
# {'no': '207/A/NBP/2026', 'effectiveDate': '2026-10-23', 'mid': 3.9247}
print("Kurs:", data['rates'][0]['mid'])  # Kurs: 3.9247
