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

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAL NOT NULL);
    """

    c.execute(query)
    conn.commit()

    insert = "INSERT INTO developers (id,name,email,salary) VALUES (1,'Radek','raj@raj.pl',5000);"
    # c.execute(insert)
    # conn.commit()

    select = "SELECT * FROM developers;"
    for row in c.execute(select):
        print(row)  # (1, 'Radek', 'raj@raj.pl', 5000.0)

except sqlite3.Error as e:
    print("Błąd:", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")
# Baza danych została podłaczona
# Połaczenie zostało zamknięte

# pgadmin, dbeaver, sqldeveloper, TablePlus, DBBrowser, DB sqlite browser
