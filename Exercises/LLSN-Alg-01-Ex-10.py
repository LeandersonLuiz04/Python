print('--------------------ARITMÉTICA--------------------------')
n1=float(input(' -Digite aqui o valor de A: '))
n2=float(input(' -muito bem, agora diga um valor para B: '))
soma=n1+n2
sub=n1-n2
produto=n1*n2
try:
    quo=(n1/n2)
except:
    if n1==0 and n2==0:
        pass
    else:
        pass
try:
    resto=n1 % n2
except:
    if n1==0 and n2==0:
        pass    
    else:
        pass
import math
try:
    log=math.log10(n1)
except:
    if n1==0 and n2==0:
        pass    
    else:
        pass
exponenciação=n1**n2
print(' a soma entre {} e {} é {} .'.format(n1,n2,soma))
print(' a subtração entre {} e {} é {} .'.format(n1,n2,sub))
print(' o produto entre {} e {} é {} .'.format(n1,n2,produto))
if n1!=0 or n2!=0:
    print(' o quociente entre {} e {} é {} .'.format(n1,n2,n1/n2))
else:
    pass
if n1!=0 or n2!=0:
    print(' o resto da divisão entre {} e {} é {} .'.format(n1,n2,n1%n2))
else:
    print(' •••••• ----Você sabe que não pode dividir por zero né?-----•••••••')
if n1!=0 or n2!=0:
    print(' o resultado do log de {} na base 10 é {}'.format(n1,math.log10(n1)))
else:
    pass
if n1==0 or n2==0:
    print(' •••••• não é possivel calcular o valor do log pois você escolheu o A valendo 0.•••••••')
print(' o resultado de {} elevado a {} é {} .'.format(n1,n2,exponenciação))
print('---------------------------------------------------------------------------------')