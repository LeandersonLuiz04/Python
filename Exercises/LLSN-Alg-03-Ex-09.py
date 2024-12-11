print('='*30)
print('     DATA DE FERIADO   ')
print('='*30)
mes=input("Diga o nome de algum mês do ano: ")
dia=int(input("Informe algum dia deste mês:  "))
if dia==1 and mes=='Janeiro':
    print(' Feriado de Confraternização Universal. ')
elif dia==21 and mes=='Abril':
    print('Feriado de Tiradentes.')
elif dia==1 and mes=='Março':
    print('Feriado do Dia do Trabalhador. ')
elif dia==7 and mes=='Setembro':
    print('Feriado da Independência do Brasil. ')
elif dia==12 and mes=='Outubro':
    print('Feriado de Nossa Senhora Aparecida. ')
elif dia==2 and mes=='Novembro':
    print('Dia de Finados')
elif dia==15 and mes=='Novembro':
    print('Feriado do dia da Proclamação da República. ')
elif dia==25 and mes=='Dezembro':
    print('Feriado de Natal. ')
else:
    print(f'O dia {dia} no mês de {mes} não corresponde a nenhum feriado nacional. ')