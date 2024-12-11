print('----------------CÍRCULOS E ESFERAS-----------------------------------------------------------------------------')
raio_circulo=float(input(' • Digite aqui o raio do círculo: '))
import math
área_circulo=math.pi*(raio_circulo)**2
círculo="{:.3f}".format(área_circulo)
raio_esfera=float(input(' • Muito bem, agora digite o raio da esfera para calcular o seu volume: '))
import math
volume_esfera=(4/3)*math.pi*(raio_esfera)**3
esfera="{:.3f}".format(volume_esfera)
print(' Você obteve um círculo com área valendo aproximadamente {} e uma esfera com volume valendo aproximadamente {}.'.format(círculo,esfera))
print('--------------------------------------------------------------------------------------------------------------------------')