#
# Jak działa REST API?
#
# Architektura REST opiera się na zasobach (np. użytkownik, produkt, zamówienie),
# które są jednoznacznie identyfikowane przez adresy URL.
# Komunikacja odbywa się za pomocą standardowych metod HTTP (czasowników):
#
# Metoda HTTP	Operacja CRUD	Co robi?
# GET	Read (Odczyt)	Pobiera dane zasobu z serwera (nie zmienia ich stanu).
# POST	Create (Tworzenie)	Tworzy nowy zasób na serwerze.
# PUT / PATCH	Update (Aktualizacja)	Aktualizuje zasób (PUT zastępuje cały obiekt, PATCH tylko jego część).
# DELETE	Delete (Usuwanie)	Usuwa wskazany zasób z serwera.
# https://github.com/public-api-lists/public-api-lists

# klient http httpx, niquests
import requests

# pip install requests


url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print(response)
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP
# <Response [200]> ok
# 3xx - warningi, przekierowania
# 4xx 404 - brak strony, 400 Bad Request
# 5xx 500 Interanal Server Error

print(response.text)  # json - str

data = response.json()  # zamiana na słownik
print(data)
print(type(data))  # <class 'dict'>

# wypisac ten kawał
print("Kawał:", data['value'])
# Kawał: jesus once walked on water;Chuck Norris once swam on land

icon_url = data['icon_url']
print(icon_url)
# https://api.chucknorris.io/img/avatar/chuck-norris.png

response_img = requests.get(icon_url)
with open('icon.png', "wb") as f:
    f.write(response_img.content)
