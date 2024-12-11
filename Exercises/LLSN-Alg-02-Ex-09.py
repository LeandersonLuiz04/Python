print('--------DATA INVERTIDA---------')
data=int(input('Digite uma data no formato DDMMAA: '))
dia=(data//10000)
mes=(data%10000)//100
ano=(data%100)
invert_data=(ano*10000)+(mes*100)+dia
print(f'O inverso desta data é {invert_data}. ')
print('-------------------------------------')