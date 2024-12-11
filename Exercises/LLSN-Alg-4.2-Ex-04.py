
logo='''

'  ┌─┐┌─┐┬─┐┬┌┬┐┌─┐┌┬┐┬─┐┌─┐  ┌┬┐┌─┐  ┌─┐┌─┐┬  ┬┌─┐┌─┐┌┐┌┌─┐┌─┐
'  ├─┘├┤ ├┬┘││││├┤  │ ├┬┘│ │   ││├┤   ├─┘│ ││  ││ ┬│ │││││ │└─┐
'  ┴  └─┘┴└─┴┴ ┴└─┘ ┴ ┴└─└─┘  ─┴┘└─┘  ┴  └─┘┴─┘┴└─┘└─┘┘└┘└─┘└─┘

'''

print(logo)
import math

valores=[]
perimetro=0
coord_anterior=None

def calculo_distancia(coord1,coord2):
    x1,y1=coord1
    x2,y2=coord2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2) 

valor_x=input("Digite a coordenada x de um ponto: ")

while valor_x!='':
    valor_x=float(valor_x)
    valor_y=float(input("Digite a coordenada y de um ponto: "))
    coordenada=(valor_x,valor_y)
    valores.append(coordenada)

    if coord_anterior:
        perimetro+=calculo_distancia(coord_anterior,coordenada)
    
    coord_anterior=coordenada 

    valor_x=input("Digite a coordenada de x(enter para sair): ")

if coord_anterior:
        perimetro+=calculo_distancia(coord_anterior,valores[0])
print(f'COORDENADAS: {valores}')
print(f'PERÍMETRO: {perimetro}')