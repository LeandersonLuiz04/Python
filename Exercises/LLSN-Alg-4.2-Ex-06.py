logo='''

'  ┓ •     ┓          • ┓   ┓  
'  ┣┓┓╋┏  ┏┫┏┓  ┏┓┏┓┏┓┓┏┫┏┓┏┫┏┓
'  ┗┛┗┗┛  ┗┻┗   ┣┛┗┻┛ ┗┗┻┗┻┗┻┗ 
'               ┛              

'''
print(logo)
import re
while True:
    
    b=input("BITS: ")
    if b=="":
        break
    if len(b)!=8 or not re.match('^[01]*$', b):
        print("Você deve digitar uma sequência de 8 bits(0 e/ou 1)!!")
        break

    contagem_um=len(re.findall(r"1",b))
    contagem_zero=len(re.findall(r"0",b))
    print(f"QUANTIDADE DE 1: {contagem_um}")
    print(f"QUANTIDADE DE 0: {contagem_zero}")
    if contagem_um%2==0:
        print(f"Bit de paridade de {b} é : 0") 
    else:
        print(f"Bit de paridade de {b} é : 1")   