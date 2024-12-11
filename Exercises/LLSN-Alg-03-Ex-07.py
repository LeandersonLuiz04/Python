print('='*30)
print('   NÍVEIS DE BARULHO   ')
print('='*30)
nivel_de_volume=int(input('Digite aqui um nível de volume sonoro em decibeis(dB): '))
if nivel_de_volume==130:
    print('O volume sonoro de 130 dB equivale ao som de uma britadeira.')
elif nivel_de_volume==106:
    print('O volume sonoro de 106 dB equivale ao som de um cortador de grama.')
elif nivel_de_volume<130 and nivel_de_volume>106:
    print('O nível deste volume está entre os barulhos de uma britadeira e um cortador de grama.')
elif nivel_de_volume==70:
    print('O volume sonoro de 70 dB equivale ao barulho de um despertador. ')
elif nivel_de_volume==40:
    print('O volume sonoro de 40 dB equivale ao barulho de uma sala silenciosa ')
elif nivel_de_volume<106 and nivel_de_volume>70:
    print('O nível deste volume está entre os barulhos de um cortador de grama e um despertador.')
elif nivel_de_volume<70 and nivel_de_volume>40:
    print('O nível deste volume está entre os barulhos de um despertador e uma sala silenciosa. ')
else:
    print('Você deve escolher um valor que esteja entre 40 até 130 decibeis. ')













#britadeira 130db
#cortador de grama 106db
#despertador 70db
#sala silenciosa 40db