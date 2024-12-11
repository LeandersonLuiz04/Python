def calcular_valor_A(N):
    A = 0  
    i = 1  
    while i <= N:
        if i % 2 == 1:
            A += 1 / i
        else:
            A -= 1 / i
        i += 1  
    return A
N = int(input("Digite um número inteiro positivo para N: "))
resultado_A = calcular_valor_A(N)
result_format='{:.3f}'.format(resultado_A)
print(f"O valor  aproximado de A é: {result_format}",)
