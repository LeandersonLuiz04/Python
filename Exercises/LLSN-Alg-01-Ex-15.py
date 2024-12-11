print('='*50)
print('      ÁREA DE POLÍGONO REGULAR    ')
print('='*50)
l=int(input('Digite aqui o comprimento de um lado do polígono: '))
n=int(input('Qual o número de lados desse polígono? : '))
import math
area=(n*l**2)/(4*math.tan(math.pi/n))
print(f'ÁREA: {area} ')
