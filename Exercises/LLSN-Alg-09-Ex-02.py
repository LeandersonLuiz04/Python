import sys
def main():

  argumentos = sys.argv[1:]

  if not argumentos:    
    print("ERRO: Nenhum arquivo especificado.")
    return
  nome_arquivo = argumentos[0]

  try:
    arquivo = open(nome_arquivo, "r")
  except FileNotFoundError:
    print(f"ERRO: Arquivo '{nome_arquivo}' não encontrado.")
    return

  linhas = arquivo.readlines()[:10]

  for linha in linhas:
    print(linha.rstrip())

  arquivo.close()

if __name__ == "__main__":
  main()
