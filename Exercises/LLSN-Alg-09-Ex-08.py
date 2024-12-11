import re

def frequencia_de_palavras(arquivo):
    try:
        with open(arquivo, 'r') as arq:
            texto = arq.read().lower()
            palavras = texto.split()

            global total_palavras
            total_palavras = len(palavras)
            frequencias_palavras = {}

            for palavra in palavras:
                if palavra in frequencias_palavras:
                    frequencias_palavras[palavra] += 1
                else:
                    frequencias_palavras[palavra] = 1

            return frequencias_palavras

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        return {}

if __name__ == "__main__":
    while True:
        nome_arquivo = input("Nome do Arquivo: ")
        if nome_arquivo == "":
            break

        frequencias_palavras = frequencia_de_palavras(nome_arquivo)
        if frequencias_palavras:
            for palavra, frequencia in frequencias_palavras.items():
                porcentagem = (frequencia / total_palavras) * 100
                print(f"{palavra}: {porcentagem:.2f}%")
        else:
            print("Nenhuma palavra encontrada no arquivo.")
