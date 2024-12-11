logo='''

┌─┐┌─┐┌┬┐┌─┐┬─┐┌─┐┌─┐
├┤ ├─┤ │ │ │├┬┘├┤ └─┐
└  ┴ ┴ ┴ └─┘┴└─└─┘└─┘

'''
print(logo)
n=int(input('Digite um número inteiro: '))
if n<2:
    print('O VALOR DEVE SER MAIOR QUE 2!!!')

fator=2
valores=[]

while fator<=n :
    if n%fator==0:
        print(fator)
        n//=fator    
    else:    
        fator+=1
