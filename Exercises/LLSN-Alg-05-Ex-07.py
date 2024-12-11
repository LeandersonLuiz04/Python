import random

def sorteia_dado():
    return random.randint(1,6)




contador=0
lista_de_valores=[0,0,0,0,0,0]
while contador<1000000:
    aleatorio=sorteia_dado()
    lista_de_valores[aleatorio-1] += 1
    contador+=1

print(f"NÚMERO DE VEZES QUE CAIU O VALOR 1:{lista_de_valores[0]}|PORCENTAGEM: {(lista_de_valores[0]/1000000)*100} %")
print(f"NÚMERO DE VEZES QUE CAIU O VALOR 2:{lista_de_valores[1]}|PORCENTAGEM: {(lista_de_valores[1]/1000000)*100} %")   
print(f"NÚMERO DE VEZES QUE CAIU O VALOR 3:{lista_de_valores[2]}|PORCENTAGEM: {(lista_de_valores[2]/1000000)*100} %")   
print(f"NÚMERO DE VEZES QUE CAIU O VALOR 4:{lista_de_valores[3]}|PORCENTAGEM: {(lista_de_valores[3]/1000000)*100} %")
print(f"NÚMERO DE VEZES QUE CAIU O VALOR 5:{lista_de_valores[4]}|PORCENTAGEM: {(lista_de_valores[4]/1000000)*100} %")
print(f"NÚMERO DE VEZES QUE CAIU O VALOR 6:{lista_de_valores[5]}|PORCENTAGEM: {(lista_de_valores[5]/1000000)*100} %")