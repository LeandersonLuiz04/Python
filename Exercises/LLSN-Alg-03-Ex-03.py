print('='*30)
print('     VOGAL OU CONSOANTE   ')
print('='*30)
letra=input('Digite aqui uma letra qualquer da lingua portuguesa: ')
vogais=['a','e','i','o','u','A','E','I','O','U']
if letra in vogais:
    print(f'A letra {letra} é uma vogal. ')
else:
    print(f'A letra {letra} é uma consoante. ')