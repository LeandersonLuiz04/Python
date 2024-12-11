print('-------CENTENAS,DEZENAS E UNIDADES---------')
n=int(input('Digite aqui um número(até 999): '))
C=(n//100)
D=(n%100)//10
U=(n%10)
print(f'CENTENA : {C}')
print(f'DEZENA : {D}')
print(f'UNIDADE : {U}')
print('-------------------------------------------')