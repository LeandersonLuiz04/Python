import re

def comentarios(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
            for linha, texto_linha in enumerate(entrada, start=1):
                
                texto_linha_sem_comentarios = re.sub(r"(^|\s)(#.*?)(?=$|\s)", r"\1", texto_linha)
                
                if texto_linha_sem_comentarios.strip():  
                    saida.write(texto_linha_sem_comentarios)

    except FileNotFoundError as erro:
        print(f"Erro: Arquivo não encontrado: {erro.filename}")

if __name__ == "__main__":
  while True:
    arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
    if not arquivo_entrada:
      break
    arquivo_saida = input("Digite o nome do arquivo de saída: ")
    if not arquivo_saida:
      break

    comentarios(arquivo_entrada, arquivo_saida)
    print(f"Resultado salvo em: {arquivo_saida}")
