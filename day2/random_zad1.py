import random

# działania na liczbach losowych

# Return random integer in range [a, b], including both end points.
print(random.randint(1, 100))  # od 1 do 100 włacznie, int

print(random.randrange(1, 100))  # od 1 do 99, int
print(random.randrange(5))  # od 0 do 4

print(random.random())  # float od 0 do 0.999999
print(random.random() * 7)  # float od 0 do 6.999999

lista = ["Radek", "Tomek", "Zenek", "Ania", "Kasia"]
print(lista[random.randrange(len(lista))])  # Kasia

print(random.choice(lista))  # Kasia, losuje jeden element

lista_kul = list(range(1, 50))
# print(lista_kul)
kula = random.choice(lista_kul)
lista_kul.remove(kula)
print(kula)  # 10

print(random.choices(lista_kul, k=6))  # [9, 28, 36, 34, 29, 28], z powtórzeniami
print(random.sample(lista_kul, k=6))
print(random.sample(lista_kul, 6))  # k: nie przepisujemy
# [48, 39, 25, 41, 23, 28]
# [34, 1, 15, 8, 6, 40]
# [18, 22, 2, 30, 35, 41]
