logo='''


'  ┌┐ ┬┌┐┌┌─┐┬─┐┬┌─┐  ┌─┐┌─┐┬─┐┌─┐  ┌┬┐┌─┐┌─┐┬┌┬┐┌─┐┬  
'  ├┴┐││││├─┤├┬┘││ │  ├─┘├─┤├┬┘├─┤   ││├┤ │  ││││├─┤│  
'  └─┘┴┘└┘┴ ┴┴└─┴└─┘  ┴  ┴ ┴┴└─┴ ┴  ─┴┘└─┘└─┘┴┴ ┴┴ ┴┴─┘


'''
print(logo)
numero_binario = input("Digite um número binário para converter para decimal: ")

numero_decimal = 0

for i in range(len(numero_binario)):

    digito = int(numero_binario[i])
    
 
    valor = digito * (2 ** (len(numero_binario) - 1 - i))
    
    numero_decimal += valor

print("O número decimal equivalente é:", numero_decimal)
