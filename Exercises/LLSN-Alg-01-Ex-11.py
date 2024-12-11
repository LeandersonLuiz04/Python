print('='*60)
print('    DISTÂNCIA ENTRE DOIS PONTOS DA TERRA    ')
print('='*60)
latitude1=int(input("Digite aqui a latitude do primeiro ponto em graus: "))
longitude1=int(input("Digite aqui a longitude do primeiro ponto em graus: "))
latitude2=int(input("Digite aqui a latitude do segundo ponto em graus: "))
longitude2=int(input("Digite aqui a longitude do segundo ponto em graus : "))
import math
latitude1_radians=math.radians(latitude1)   #t1
longitude1_radians=math.radians(longitude1)  #g1
latitude2_radians=math.radians(latitude2)    #t2
longitude2_radians=math.radians(longitude2)  #g2

distancia = 6371.01*math.asin(math.sin(latitude1_radians)*math.sin(latitude2_radians) + math.cos(latitude1_radians)*math.cos(latitude2_radians)*math.cos(longitude1_radians-longitude2_radians))

print(f'A distância entre os pontos {(latitude1,longitude1)} e {latitude2, longitude2}, é igual {distancia}km')





#distancia = 6371.01 × arccos(sen(t1) sen(t2) + cos(t1) cos(t2) × cos(g1 − g2))