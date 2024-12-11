logo='''

╔═╗┬┌─┐┬─┐┌─┐  ┌┬┐┌─┐  ┌─┐┌─┐┌─┐┌─┐┬─┐
║  │├┤ ├┬┘├─┤   ││├┤   │  ├┤ └─┐├─┤├┬┘
╚═╝┴└  ┴└─┴ ┴  ─┴┘└─┘  └─┘└─┘└─┘┴ ┴┴└─

'''

print(logo)

alfabeto=['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

interação_usuario=input("Escreva 'encode' para encriptar a mensagem e 'decode' para decifra-la:  ")
mensagem=input('Escreva a mensagem: ').lower()
pular=int(input("Quantas letras você deseja pular/retornar: "))

def cifra(msg, jump):
    cifra_cesar=""
    for letter in msg:
        if letter in alfabeto:
            posição=alfabeto.index(letter)
            if interação_usuario=='encode':
            
                posição_nova=posição+jump
                letra=alfabeto[posição_nova]
                cifra_cesar+=letra       
        
            else:       
                posição_nova=posição-jump         
                letra=alfabeto[posição_nova]
                cifra_cesar+=letra
    
        else:
            cifra_cesar+=letter
    
    print(f'MENSAGEM: {cifra_cesar} .')
cifra(msg=mensagem, jump=pular)

