logo='''
'  ┌┬┐┌─┐┌┬┐┬┌─┐  ┌─┐┬─┐┬┌┬┐┌┬┐┌─┐┌┬┐┬┌─┐┌─┐
'  │││├┤  │││├─┤  ├─┤├┬┘│ │ │││├┤  │ ││  ├─┤
'  ┴ ┴└─┘─┴┘┴┴ ┴  ┴ ┴┴└─┴ ┴ ┴ ┴└─┘ ┴ ┴└─┘┴ ┴
'''
print(logo)
import os
lista_de_valores=[]
contador=0
print('---PARA CANCELAR DIGITE 0----')
while True:
    n=input('Digite aqui os valores para calcular a média(0 para cancelar): ')
    if n=='0':
        break
    os.system('cls') or None 
    num=int(n)
    lista_de_valores.append(num)
    print(f'LISTA DE NOTAS: {lista_de_valores}')
    contador+=1
    media=sum(lista_de_valores)/contador
    print(f'MÉDIA: {media}')
