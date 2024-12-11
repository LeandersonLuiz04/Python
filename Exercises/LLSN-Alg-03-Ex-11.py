print('='*30)
print('     Equação do segundo grau      ')
print('='*30)
a=float(input('Digite aqui um valor para a: '))
b=float(input('Digite aqui um valor para b: '))
c=float(input('Digite aqui um valor para o c: '))
delta=(b**2)-4*a*c
if a==0:
    print('O valor de a deve ser diferente de 0.')
elif delta<0:
    print('A equação não possui raízes reais. ')
else:
    import math
    delta=(b**2)-4*a*c
    raiz1=(-b+(math.sqrt(delta)))/2*a
    raiz2=(-b-(math.sqrt(delta)))/2*a
    print(f'Essa equação do segundo grau tem como raízes {raiz1} e {raiz2} .')
