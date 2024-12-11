print('-------UNIDADES DE TEMPO------------')
dias=int(input('Digite aqui o número de dias: '))
horas=int(input('Digite aqui o número de horas: '))
min=int(input('Digite aqui os minutos: '))
seg=int(input('Digite aqui os segundos: '))
total=(dias*86400)+(horas*3600)+(min*60)+seg
print(f'O total é de {total} segundos.')
print('----------------------------------------')