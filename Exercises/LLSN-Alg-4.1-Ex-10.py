N = int(input("Digite um número inteiro positivo: "))

if N <= 0:
    print("O número fornecido deve ser positivo.")
else:
    A = 0
    i = 1
    while i <= 2 * N - 1:
        A += 1 / i
        i += 2
    print("O valor de A é:", A)
