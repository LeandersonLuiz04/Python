import re

def ortografia(arquivo_entrada, palavras_portugues):
    try:
        with open(palavras_portugues, 'r', encoding='utf-8') as port:
            dicionario = set(word.strip().lower() for word in port)
        
        with open(arquivo_entrada, 'r', encoding='utf-8') as arq:
            texto = arq.read()
            texto = re.sub(r"[^\w\s]", "", texto)  
            palavras = texto.lower().split()  # Dividindo o texto em palavras
            palavras_erradas = [palavra for palavra in palavras if palavra not in dicionario]
            
            if palavras_erradas:
                print("Palavras encontradas com erros ortográficos:")
                for palavra in palavras_erradas:
                    print(palavra)
                print(f"Número de palavras erradas: {len(palavras_erradas)}")
            else:
                print("Nenhuma palavra com erro ortográfico encontrada.")
    
    except FileNotFoundError as erro:
        print(f"Erro: Arquivo não encontrado: {erro.filename}")

if __name__ == "__main__":
    arquivo_verificar = input("Digite o nome do arquivo que deseja verificar: ")
    arquivo_dicionario = input("Digite o nome do arquivo onde se encontra o dicionário: ")
    ortografia(arquivo_verificar, arquivo_dicionario)
