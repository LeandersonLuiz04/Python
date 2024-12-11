print('-------INVERSO DE CDU----------------')
n=int(input('Digite aqui um valor até 999: '))
C=n//100
D=(n%100)//10
U=(n%10)
result=(U*100)+(D*10)+C
print(f' O inverso é {result}. ')
print('------------------------------------')