import re

def text(mensagem):
    lista=[]
    list_text=mensagem.split()

    for palavra in list_text:
        palavra=re.sub('[?!., ]',"",palavra)    
        lista.append(palavra)
    print(lista)
def main():
    msg=input("TEXTO: ")
    text(mensagem=msg)

if __name__=="__main__":
    main()