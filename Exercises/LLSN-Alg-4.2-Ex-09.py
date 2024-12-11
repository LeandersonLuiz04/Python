logo='''

'  ┬─┐┌─┐┬┌─┐  ┌─┐ ┬ ┬┌─┐┌┬┐┬─┐┌─┐┌┬┐┌─┐
'  ├┬┘├─┤│┌─┘  │─┼┐│ │├─┤ ││├┬┘├─┤ ││├─┤
'  ┴└─┴ ┴┴└─┘  └─┘└└─┘┴ ┴─┴┘┴└─┴ ┴─┴┘┴ ┴

'''
print(logo)
def calcular_raiz_quadrada(x):
    raiz = x / 2.0

    precisao = 0.0001
    
    while abs(raiz * raiz - x) > precisao:

        raiz = (raiz + x / raiz) / 2.0
    return raiz

x = float(input("Digite um número para calcular a raiz quadrada: "))

raiz_quadrada = calcular_raiz_quadrada(x)
print(f"A raiz quadrada de {x} é igual/aproximadamente a {raiz_quadrada:.3f}")
