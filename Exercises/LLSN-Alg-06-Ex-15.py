import re

def token(expressão):
    lista_de_token=[]
    expressão = re.sub(r'\s+',"", expressão)
    possibilidades=r'(|\(|\)|[+\-*/^])'
    x=re.findall(possibilidades,expressão)
    lista_de_token.append(x)

    return lista_de_token


def main():
    exp=input("EXPRESSÃO: ")
    print(f"LISTA DE TOKENS: {token(expressão=exp)}")
    

if __name__=="__main__":
    main()
