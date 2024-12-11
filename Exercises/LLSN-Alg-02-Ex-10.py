matricula=int(input('Digite aqui o número de matrícula do aluno no formato AASDDD: '))
ano=(matricula//10000)
s=(matricula%10000)//1000
d=(matricula%1000)
print(f'Este aluno está matriculado no {ano}° ano, no {s}° semestre e sua ordem de matrícula é {d}.')