# baza danych - system przechowywania i przetwarzania danych, silnik
# bazy relacyjne i nierelacyjne
# sql , nosql
# mysql, postgres, Ms sql, db2, oracle, terradata
# sqlite

import sqlite3

try:
    conn = sqlite3.connect("baza_danych.db")
    c = conn.cursor()
    print("Baza danych została podłaczona")
except sqlite3.Error as e:
    print("Błąd:", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")
# Baza danych została podłaczona
# Połaczenie zostało zamknięte