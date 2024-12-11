def encaixa(a,b):

    a_string=str(a)
    if a_string.endswith(str(b)):
        return "Encaixa"
    else:
        return "Não encaixa"
    
valor_a=int(input("Valor de A: "))
valor_b=int(input("Valor de B: "))
print(encaixa(valor_a,valor_b))

