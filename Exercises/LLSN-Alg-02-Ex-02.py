print('='*30)
print('{:^30}'.format('TROCO'))
print('='*30)
valorapagar=int(input('Digite aqui o total que deve ser pago em centavos:  '))
valorentregue=int(input('Digite aqui quantos centavos você depositou na máquina: '))
troco=valorapagar-valorentregue
result=[50,25,10,5,1]
