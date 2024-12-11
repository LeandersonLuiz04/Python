
lista=[]
while True:
    numero=int(input("NÚMERO(para cancelar digite 0): "))
    if numero==0:
        break
    else:
        lista.append(numero)
        lista.sort()
        print(lista)