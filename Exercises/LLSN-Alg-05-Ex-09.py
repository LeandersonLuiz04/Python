escolha_ano=int(input("ANO: "))
def eh_bissexto(ano):
    if ano%4==0 and ano%100!=0:
        print(f" O ANO DE {ano} É BISSEXTO: ")
    else:
        print(f"O ANO DE {ano} NÃO É BISSEXTO ")
eh_bissexto(escolha_ano)