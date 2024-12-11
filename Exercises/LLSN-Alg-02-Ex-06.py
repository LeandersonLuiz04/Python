print('-------SOMA DOS DÍGITOS------------')
n=int(input('Digite aqui um número com 4 dígitos: '))
M=(n//1000)
C=(n%1000)//100
D=(n%100)//10
U=(n%10)
soma=(M+C+D+U)
print(f'A soma dos dígitos vale {soma}. ')
