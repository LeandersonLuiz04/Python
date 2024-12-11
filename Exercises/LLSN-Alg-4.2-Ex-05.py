logo='''


███████ ███    ██ ████████ ██████   █████  ██████   █████  ███████ 
██      ████   ██    ██    ██   ██ ██   ██ ██   ██ ██   ██ ██      
█████   ██ ██  ██    ██    ██████  ███████ ██   ██ ███████ ███████ 
██      ██  ██ ██    ██    ██   ██ ██   ██ ██   ██ ██   ██      ██ 
███████ ██   ████    ██    ██   ██ ██   ██ ██████  ██   ██ ███████ 
                                                                   
                                                                   
'''
print(logo)
lista_de_idades=[]
custo=[]

while True:
    idd=input('DIGITE A IDADE DOS MEMBROS DO GRUPO: ')
    if idd=='':
        break
    idade=int(idd)
    lista_de_idades.append(idade)
    
    if idade<=2:
        pagamento=0
    elif idade>=3 and idade<=12:
        pagamento=14
    elif idade>=65:
        pagamento=18
    else:
        pagamento=23    
    
    custo.append(pagamento)
    valor=sum(custo)
    valor_format='{:.2f}'.format(valor)
    
    print(f'IDADES: {lista_de_idades} ')
    print(f'VALOR: R${valor_format}')
    print('---PARA CANCELAR PRESSIONE ENTER--- ')
