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

url = "https://api.chucknorris.io/jokes/random"