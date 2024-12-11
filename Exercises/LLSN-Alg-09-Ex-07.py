import re

def frequencia_de_letras(arquivo):

    try:
        with open(arquivo, 'r') as arq:
            texto = arq.read().lower()  
            sem_espaco = re.sub(r"\s", "", texto)
            global total
            total=0
            frequencias = {}  
            for letra in sem_espaco:
                total+=1
                if letra in frequencias:
                    frequencias[letra] += 1  
                else:
                    frequencias[letra] = 1  
        return frequencias

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        return {}
if __name__ == "__main__":
    while True:
        nome_arquivo = input("Nome do Arquivo: ")
        if nome_arquivo == "":
            break

        frequencias_letras = frequencia_de_letras(nome_arquivo)
        if frequencias_letras:
            for letra, frequencia in frequencias_letras.items():
                
                porcentagem=(frequencia / total)*100
                print(f"{letra}: {porcentagem:.2f}%")
        else:
            print("Nenhuma letra encontrada no arquivo.")
