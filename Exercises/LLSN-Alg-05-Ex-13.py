def encaixa(a, b):
    while b != 0 and a % 10 == b % 10:
        a //= 10
        b //= 10

    if b == 0:
        return True
    else:
        return False

def main():
    entrada=input("Digite dois números inteiros e positivos separados por espaço: ")
    numeros = entrada.split()    
    # O SPLIT DIVIDE STRINGS, EM SEGUIDA ADICIONEI EM a E b passando para inteiros
    if len(numeros) != 2:
        print("Por favor, insira exatamente dois números separados por espaço.")
        return
    
    a = int(numeros[0])
    b = int(numeros[1])
    
    maior = max(a, b)
    menor = min(a, b)

    encontrou_seg = False
    while maior >= menor:
        if encaixa(maior, menor):
            encontrou_seg = True
        maior //= 10

    if encontrou_seg:
        print(f"{b} é segmento de {a}")
    else:
        print(f"{b} não é segmento de {a}")

if __name__ == "__main__":
    main()
