valores=[]
espaço=" "
while True:
    inteiro=input("NÚMERO: ")
    if inteiro=="":
        break
    else:
        inteiro=int(inteiro)
        valores.append(inteiro)
        valores.sort(reverse=True)
print(valores[::-1])