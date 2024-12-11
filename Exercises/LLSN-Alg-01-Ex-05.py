print('='*30)
print('   RETORNO DE RECICLÁVEIS    ')
print('='*30)
vasilhames1=int(input('Digite aqui a quantidade de vasilhames menores que 1L: '))
vasilhames2=int(input('Digite aqui a quantidade de vasilhames maiores que 1L: '))
total=(vasilhames1*0.10)+(vasilhames2*0.25)
import math
total_formatado='{:.2f}'.format(total)
print(f'Você retornou ao estabelecimento {vasilhames1} vasilhames menores que um litro e {vasilhames2} vasilhames maiores que um litro, o total de créditos que você terá é de: R${total_formatado}')

