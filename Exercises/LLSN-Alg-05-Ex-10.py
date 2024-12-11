
def conta_digitos(n,d):    
    contador=0
    n_string=str(n)
    
    for digito in n_string:
        if int(digito)==d:
            contador+=1
    return contador


numero=int(input("VALOR DE N: "))
digito=int(input("VALOR DE D: "))
result=(conta_digitos(numero,digito))
print(f"O número de vezes que o número {digito} aparece em {numero} é : {result}")
