def numerar_linhas(arquivo_entrada, arquivo_saida):
  try:
    with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
      for numero_linha, linha in enumerate(entrada, start=1):
        saida.write(f"{numero_linha}: {linha}")
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

    numerar_linhas(arquivo_entrada, arquivo_saida)
    print(f"Numeração de linhas concluída. Resultado salvo em: {arquivo_saida}")
