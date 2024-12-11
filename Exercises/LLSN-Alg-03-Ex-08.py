print('='*30)
print('     NOTAS PARA FREQUÊNCIA    ')
print('='*30)
frequencia_base={
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88
}
notas=input('Digite a nota musical(C,D,E,F,G,A OU B): ').upper()
oitava=int(input('Digite a oitava(1 até 8): '))
if notas in frequencia_base:
    result=(frequencia_base[notas])*(2**(oitava-4))
    print(f'FREQUÊNCIA DA NOTA {notas}{oitava} É : {result}')
else:
    print(" FIM DO PROGRAMA " )
