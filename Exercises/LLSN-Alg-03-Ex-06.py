print('='*30)
print('   Classificando Triângulos  ')
print('='*30)
l1=int(input('Qual é o comprimento do primeiro lado deste triângulo? : '))
l2=int(input('Qual é o comprimento do segundo lado deste triângulo? : '))
l3=int(input('Qual é o comprimento do terceiro lado deste triângulo? : '))

if l1==l2 and l1==l3:
    print(f'O triângulo possui medidas iguais a, respectivamente, {l1},{l2} e {l3}, portanto, este é um triângulo equilátero. ')
elif l1==l2 or l2==l3:
    print(f'O triângulo possui medidas iguais a, respectivamente, {l1},{l2} e {l3}, portanto, este é um triângulo isósceles. ')
else:
    print(f'O triângulo possui medidas iguais a, respectivamente, {l1},{l2} e {l3}, portanto, este é um triângulo escaleno. ')