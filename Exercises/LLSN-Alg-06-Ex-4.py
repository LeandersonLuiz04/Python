palavras=[]
while True:
    resposta=input("PALAVRA: ")
    if resposta=="":
        break
    else:
        palavras.append(resposta)  
        print(palavras)
        palavras=list(set(palavras))


for i in palavras:
    print(i)