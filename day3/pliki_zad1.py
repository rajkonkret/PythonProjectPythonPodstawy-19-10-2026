# działania z plikami
# filehandler

# context manager
# with - context manager w pythonie

# open()
# encoding="utf-8" - kodowanie znaków w pliku
with open("test.log", "w", encoding="utf-8") as file:
    file.write("Powitanie\n")
    file.write("Powitanie jeszcze jedno\n")

# file.write("")  # ValueError: I/O operation on closed file.

# # "x" FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x", encoding="utf-8") as file:
#     file.write("Powitanie\n")
#     file.write("Powitanie jeszcze jedno\n")

with open("test.log", "w", encoding="utf-8") as file:
    file.write("Powitanie\n")
    file.write("Dodane\n")
    file.write("Powitanie jeszcze jedno\n")

# a - append - dołacza dane na końcu
with open("test.log", "a", encoding="utf-8") as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dośdane\n")

with open("test.log", "r", encoding="utf-8") as f:
    lines = f.read()

print(lines)
# Powitanie
# Dodane
# Powitanie jeszcze jedno
# Dodane
# Dodane
# Dośdane
