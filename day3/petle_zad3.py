# while - petla sterowana warunkiem

# pętla nieskońćzona
# while True:
#     print("Komunikat")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)  # 11
print(50 * "-")

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
