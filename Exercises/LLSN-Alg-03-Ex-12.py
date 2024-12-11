print('='*30)
print('    ANO BISSEXTO   ')
print('='*30)
ano=int(input('Digite aqui algum ano: '))
if ano%400==0:
    print(f'O ano de {ano} é bissexto. ')
elif ano%100==0:
    print(f'O ano de {ano} não é bissexto. ')
elif ano%4==0:
    print(f'O ano de {ano} é bissexto. ')
else:
    print(f'O ano de {ano} não é bissexto. ')