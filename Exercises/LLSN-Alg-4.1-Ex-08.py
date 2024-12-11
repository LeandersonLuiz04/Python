lista_de_numeros=[]
contador=0
while contador<10:

    n=int(input('Digite a nota: '))
    lista_de_numeros.append(n)
    print(lista_de_numeros)
    
    maior=max(lista_de_numeros)
    
    menor=min(lista_de_numeros)
    
    contador+=1
    
    media=sum(lista_de_numeros)/contador
    media_format='{:.2f}'.format(media)
    
    print(f"MAIOR NOTA: {maior}") 
    print(f"MENOR NOTA: {menor}")
    print(f"MÉDIA: {media_format}")