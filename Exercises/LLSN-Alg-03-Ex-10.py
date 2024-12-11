#letra==coluna
#numero==linha
print('='*30)
print('    TABULEIRO DE XADREZ   ')
print('='*30)
numero=int(input('Digite um número de 1 até 8: '))
letra=input('Diga uma letra do alfabeto de A até H: ')
comeca_preto=['a','c','e','g','A','C','E','G']
quadrados_brancos_do_a=[2,4,6,8]
quadrados_brancos_do_b=[1,3,5,7]
quadrados_brancos_do_c=[2,4,6,8]
quadrados_brancos_do_d=[1,3,5,7]
quadrados_brancos_do_e=[2,4,6,8]
quadrados_brancos_do_f=[1,3,5,7]
quadrados_brancos_do_g=[2,4,6,8]
quadrados_brancos_do_h=[1,3,5,7]


if letra in comeca_preto:
    print('Começa no Quadrado Preto. ')
else:
    print('Começa no Quadrado Branco')
if numero in quadrados_brancos_do_a and letra=='a':
    print('Termina no Quadrado Branco')
elif numero in quadrados_brancos_do_b and letra=='b': 
    print('Termina no Quadrado Branco')
elif numero in quadrados_brancos_do_c and letra=='c':
    print('Termina no Quadrado Branco')
elif numero in quadrados_brancos_do_d and letra=='d':
    print('Termina no Quadrado Branco')
elif numero in quadrados_brancos_do_e and letra=='e':
    print('Termina no Quadrado Branco')
elif numero in quadrados_brancos_do_f and letra=='f':
    print('Termina no Quadrado Branco')
elif numero in quadrados_brancos_do_g and letra=='g':
    print('Termina no Quadrado Branco')
elif numero in quadrados_brancos_do_h and letra=='h':
    print('Termina no Quadrado Branco')
else:
    print('Termina no Quadrado Preto')