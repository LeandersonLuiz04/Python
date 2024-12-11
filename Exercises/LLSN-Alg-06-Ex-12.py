def ordem(lista):
    if lista==sorted(lista):
        return True
    else:
        return False

def main():
    lista_de_numeros=[]
    while True:
        numero=input("Valor: ")
        if numero=="":
            break
        else:
            numero=int(numero)
            lista_de_numeros.append(numero)
    a=ordem(lista=lista_de_numeros)
    print(a)
if __name__=="__main__":
    main()