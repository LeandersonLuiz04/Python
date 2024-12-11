N = int(input("Digite um número inteiro positivo: "))
if N <= 0:
    print("O número fornecido deve ser positivo.")
else:
    A = 0
    for i in range(N, 0, -1):
        A += i / (N - i + 1)
    print("O valor de A é:", A)
