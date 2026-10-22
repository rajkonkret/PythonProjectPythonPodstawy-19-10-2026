import pakiet

print(40 * "-")
# AttributeError: module 'pakiet' has no attribute 'powitanie'
# pakiet.powitanie()

from pakiet import fun

print(40 * "-")
#  ----------------------------------------
fun.powitanie()  # Cześć

import pakiet.fun as pk  # jako alias

pk.powitanie()  # Cześć

# po dodaniu w __init__.py metoda info() jest widoczna
pakiet.info()
# Numer pakietu: 2.134.56.78