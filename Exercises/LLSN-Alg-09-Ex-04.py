import sys

def concatenar_arquivos(arquivos):

  for arquivo in arquivos:
    try:
      with open(arquivo, 'r') as arq:
        conteudo = arq.read()
        print(conteudo)
    except FileNotFoundError:
      print(f"Erro: Arquivo '{arquivo}' não encontrado.")
      continue

if len(sys.argv) < 2:
  print("Erro: Nenhum arquivo foi passado como argumento.")
  sys.exit(1)

arquivos = sys.argv[1:]
concatenar_arquivos(arquivos)
