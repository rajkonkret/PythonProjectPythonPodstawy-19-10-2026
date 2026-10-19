tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))

# Return a copy of the string converted to uppercase.
# teksty są niemutowalny
tekst.upper()  # nie zmienia oryginału
print(tekst)  # Witaj Świecie

# wyswietlenie kopii
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst_upper)  # WITAJ ŚWIECIE

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie
print(tekst.title())  # Witaj Świecie

print(tekst)  # Witaj Świecie
print(len(tekst))  # len() - długośc tekstu, 13 liter

# Witaj Świecie
# 01234567890... numerowanie od zera

print(tekst[0])
print(tekst[1])
print(tekst[3])
# W
# i
# a

print(tekst.index("a"))  # index 3

# "e"
print(tekst.index("e"))  # index 9, pierwszzy z lewej
print(tekst.count("e"))  # występuje 2 razy

# "w"
print(tekst.lower().count("w"))  # występuje 2 razy

# Witaj Świecie
# 01234567890... numerowanie od zera
print(tekst.count("j", 0, 4))  # wystepuje 0, z prawej zbiór otwarty -> 0123
print(tekst.count("a", 3, 4))  # wystepuje 1 raz

print(tekst.removeprefix("Witaj"))  # ' Świecie'
print(tekst.removesuffix("Świecie"))  # 'Witaj '

# strip() - usunięcie białych znaków, wiodących i kończących spacji
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode("utf-8")
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'> typ bajtowy
# \xc5\x9a kod Ś w unicode
# \x znak w sytemie szesnastkowym

print(encode_s.decode('utf-8'))  # Witaj Świecie


