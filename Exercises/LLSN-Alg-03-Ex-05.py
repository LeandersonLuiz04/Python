print('='*30)
print('    DIAS DO MÊS    ')
print('='*30)
nome_do_mes=input('Diga o nome de algum mês do ano: ')
if nome_do_mes=='fevereiro':
    print(f'O mês de {nome_do_mes} possui 28 ou 29 dias.')
elif nome_do_mes=='janeiro' or nome_do_mes=='março' or nome_do_mes=='maio' or nome_do_mes=='julho' or nome_do_mes=='agosto' or nome_do_mes=='outubro' or nome_do_mes=='dezembro':
    print(f'O mês {nome_do_mes} possui 31 dias. ')
else:
    print(f'O mês de {nome_do_mes} tem 30 dias.')                        


