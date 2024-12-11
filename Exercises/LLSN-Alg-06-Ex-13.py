
def countRange(lista,valor_min,valor_max):
    result=[]
    for i in lista:
        if int(i)>=valor_min and int(i)<valor_max:
            result.append(int(i))
    print(f"Valores maiores ou iguais ao valor {valor_min} e menor que {valor_max}: {result}")
def main():
    valores=[]
    while True:
        numero=input("Número: ")
        if numero=="":
            break
        else:
            valores.append(str(numero))
    minimo=int(input("Valor minimo: "))
    maximo=int(input("Valor máximo: "))
    countRange(lista=valores,valor_min=minimo,valor_max=maximo)
if __name__=="__main__":
    main()
