print('='*30)
print('   IDADE CANINA   ')
print('='*30)

id_cachorro=int(input('Digite aqui a idade de cachorro em anos humanos: '))

if id_cachorro<0:
    print('A idade não pode ser negativa')

elif id_cachorro<=2:
    age=id_cachorro*10.5
    print(f'A idade do cachorro em anos caninos é: {age} ')

else:
    age = (2 * 10.5) + ((id_cachorro) - 2) * 4
    print(f'A idade do cachorro em anos caninos é: {age} ')

