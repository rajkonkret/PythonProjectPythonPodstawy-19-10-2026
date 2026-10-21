# od pythona 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.strip().casefold():
    case "python":
        lista.append("Znam pythona")
    case "java":
        lista.append("Znam jave")
    case "c":
        lista.append("Znam C")
    case _:  # odpowiednik else
        print("Nie znam")

print(lista)
# Podaj znany Ci język programowaniajava
# ['Znam jave']
