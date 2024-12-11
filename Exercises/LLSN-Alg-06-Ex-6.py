def divisores(numero):
    lista=[]
    fator=2
    while fator<=numero :
        if numero%fator==0:
            lista.append(fator)
            numero//=fator
        else:    
            fator+=1
    print(f"LISTA DE DIVISORES: {lista}")

def main():
    num=int(input("Valor: "))
    divisores(numero=num)
if __name__=="__main__":
    main()