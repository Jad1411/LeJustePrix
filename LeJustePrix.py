import random
b = random.randint(1, 10)
n = input("Comment t'appelles tu?")
a = int(input("Devinez un prix entre 1 et 10."))
for k in range(1, 5):
    if a < b:
        print("C'est +")
        print("Nombre d'essai restants:", 5 - k)
        a = int(input("réessaye"))
    elif a > b:
        print("C'est -")
        print("Nombre d'essai restants:", 5 - k)
        a = int(input("réessaye"))
    elif a == b:
        print("C'est JUSTE!!!!!!!")
        print("BRAVO")
        exit()
print(f"{n},c'est raté")
exit()
