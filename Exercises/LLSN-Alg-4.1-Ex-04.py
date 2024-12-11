N=int(input("Digite um número inteiro e positivo: "))
if N<=0:
    print("O número deve ser maior que zero")
else:
    A=0
    for i in range(1,N+1):
        A+=1/i
    print(f"O valor de A é : {A}")