print('='*30)
print('    POLÍGONOS REGULARES   ')
print('='*30)
lados=int(input('Digite aqui a quantidade de lados de um polígono: '))
if lados==3:
    print(f'Um polígono com {lados} lados é um triângulo. ')
elif lados==4:
    print(f'Um polígono com {lados} lados é um quadrilátero. ')
elif lados==5:
    print(f'Um polígono com {lados} lados é um pentágono. ')
elif lados==6:
    print(f'Um polígono com {lados} lados é um hexágono. ')
elif lados==7:
    print(f'Um polígono com {lados} lados é um heptágono. ')
elif lados==8:
    print(f'Um polígono com {lados} lados é um octógono. ')
elif lados==9:
    print(f'Um polígono com {lados} lados é um eneágono. ')
elif lados==10:
    print(f'Um polígono com {lados} lados é um decágono. ')
else:
    print(' Você deve escolher uma quantidade de lados maior ou igual a 3. ')