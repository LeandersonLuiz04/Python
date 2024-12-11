import sys

def palavra_longa(arquivo):

  try:
    with open(arquivo, 'r') as arq:
      todas_palavras = arq.read().split()
      maior_palavra = max(todas_palavras, key=len)
      print(f"A maior palavra é: {maior_palavra}")
      print(f"Seu número de letras: {len(maior_palavra)}")
  except FileNotFoundError:
    print(f"Erro: Arquivo '{arquivo}' não encontrado.")

if __name__ == "__main__":
  while True:
    arquivo = input("Digite o nome do arquivo: ")
    if arquivo=='':
      break
    palavra_longa(arquivo)

    