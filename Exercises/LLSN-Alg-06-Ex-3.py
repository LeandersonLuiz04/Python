def remover_extremos(lista, n):
    if len(lista) < 2 * n:
        raise ValueError("A lista não tem elementos suficientes para remover os extremos.")
    lista_ordenada = sorted(lista)
    nova_lista = lista_ordenada[n:-n]
    return nova_lista

def main():
    entrada = input("Digite uma lista de números separados por espaço: ")
    lista = list(map(float, entrada.split()))
    if len(lista) < 4:
        print("A lista deve conter pelo menos 4 valores.")
        return

    n = 2
    try:
        lista_sem_extremos = remover_extremos(lista, n)
        print("Lista original:", lista)
        print("Lista sem os 2 maiores e 2 menores valores:", lista_sem_extremos)
    except ValueError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
