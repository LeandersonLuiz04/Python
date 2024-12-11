logo='''

'  ┌─┐┌─┐┬─┐┌─┐  ┌─┐┬ ┬  ┌─┐┌─┐┬─┐┌─┐┌─┐
'  │  ├─┤├┬┘├─┤  │ ││ │  │  │ │├┬┘│ │├─┤
'  └─┘┴ ┴┴└─┴ ┴  └─┘└─┘  └─┘└─┘┴└─└─┘┴ ┴

'''
print(logo)
import random

num_simulacoes = 10
total_sorteios = 0

for _ in range(num_simulacoes):
    resultados = ''
    sequencia = 0

    while 'AAA' not in resultados and 'OOO' not in resultados:
        resultado = random.choice(['A', 'O'])
        resultados += resultado
        sequencia = sequencia + 1 if len(resultados) >= 2 and resultado == resultados[-2] else 1

    total_sorteios += len(resultados)
    print(f"{resultados} ({len(resultados)} sorteios)")

media_sorteios = total_sorteios / num_simulacoes
print(f"\nNa média, foram necessários {media_sorteios:.1f} sorteios.")
