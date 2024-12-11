import re

def letras(arquivo):

    try:
        with open(arquivo, 'r') as arq:
            texto = arq.read().lower()  
            texto = re.sub(r"(^|\s)(#.*?)(?=$|\s)", r"\1", texto)
            letras_alfabeto={}
            for letra in ("abcdefghijklmnopqrstuvwxyz"):
                letras_alfabeto[letra]=0
            for letra in texto:
                if letra in letras_alfabeto:
                    letras_alfabeto[letra] += 1  
                else:
                    letras_alfabeto[letra] = 1  
        return letras_alfabeto

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        return {}
if __name__ == "__main__":
    while True:
        nome_arquivo = input("Nome do Arquivo: ")
        if nome_arquivo == "":
            break

        frequencias_letras = letras(nome_arquivo)
        if frequencias_letras:
            for letra, frequencia in frequencias_letras.items():

                print(f"{letra}: {frequencia}")
        else:
            print("Nenhuma letra encontrada no arquivo.")


