# with open("test.log", "r") as f:
#     lines = f.read()
#
# print(lines)
# Powitanie
# Dodane
# Powitanie jeszcze jedno
# Dodane
# Dodane
# DoĹ›dane

import chardet

# pip install chardet

# odczyt binarny - rb
with open('test.log', "rb") as fh:
    raw_data = fh.read()

print(raw_data)
# b'Powitanie\r\nDodane\r\nPowitanie jeszcze jedno\r\nDodane\r\nDodane\r\nDo\xc5\x9bdane\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'utf-8', 'confidence': 0.8325714285714286, 'language': 'pl', 'mime_type': 'text/plain'}
encoding = result['encoding']
print("Kodowanie:", encoding)

print(50 * "-")
print(raw_data.decode(encoding=encoding))
# --------------------------------------------------
# Powitanie
# Dodane
# Powitanie jeszcze jedno
# Dodane
# Dodane
# Dośdane
# charset_normalizer
