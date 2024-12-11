print("-------------ÁREA DE TRIÂNGULOS------------------------------------")
L1 = float(input("digite aqui o valor do primeiro lado do triângulo: "))
L2 = float(input("digite aqui o valor do segundo lado do triângulo: "))
L3 = float(input("digite aqui o valor do último lado deste triângulo: "))
L = (L1+L2+L3)/2
área = L*(L-L1)*(L-L2)*(L-L3)
import math
raiz_q = math.sqrt(área)
formatted_num = "{:.3f}".format(raiz_q)
print(" A área deste triângulo é de aproximadamente", formatted_num,"metros cúbicos.")
print("---------------------------------------------------------------------")