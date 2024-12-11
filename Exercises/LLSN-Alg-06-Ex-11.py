import random
lista=[]
while len(lista)<6:
    aleatorio=random.randint(1,60)
    if aleatorio not in lista:
        lista.append(aleatorio)
    lista.sort()
print(lista)