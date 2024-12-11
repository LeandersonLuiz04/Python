def eh_perfeito(n):
    if n < 1:
        return False
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i

    return soma_divisores == n
def main():
    print("Números perfeitos de 1 a 10.000:")
    for numero in range(1, 10001):
        if eh_perfeito(numero):
            print(numero)
if __name__ == "__main__":
    main()
