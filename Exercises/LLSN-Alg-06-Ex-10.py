def formatar_lista(lista):
    if not lista:
        return ""
    return ', '.join(lista[:-1]) + ' e ' + lista[-1] if len(lista) > 1 else lista[0]

def main():
    lista_palavras = []
    print("Digite palavras para adicionar à lista (Enter para cancelar):")
    
    while True:
        palavra = input("Digite uma palavra: ")
        if palavra == "":
            break
        lista_palavras.append(palavra)
    
    if lista_palavras:
        resultado = formatar_lista(lista_palavras)
        print(f"{resultado}")
    else:
        print("Nenhuma palavra foi inserida.")

if __name__ == "__main__":
    main()
