logo='''

┌─┐┌─┐┬  ┬┌┐┌┌┬┐┬─┐┌─┐┌┬┐┌─┐
├─┘├─┤│  ││││ ││├┬┘│ │││││ │
┴  ┴ ┴┴─┘┴┘└┘─┴┘┴└─└─┘┴ ┴└─┘

'''
print(logo)

alfabeto=['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
contador=0

while True: 
    palavra=input('Digite uma palavra: ')
    if palavra=='':
        break
    a=palavra[::-1]    
    if a==palavra:
        print(f"A palavra {palavra} é um palíndromo. ")
    else:
        print(f"A palavra {palavra} não é um palíndromo. ")
       

















#Uma string é considerada um palíndromo se, de trás para frente, ela for idêntica à string original.