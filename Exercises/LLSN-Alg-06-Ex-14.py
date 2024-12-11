possibilidades={
    "+":1,
    "-":1,
    "*":2,
    "^":3,
}

def precedencia(operador):
    return possibilidades[operador]

def main():
    opera=input("OPERADOR: ")

    if opera in possibilidades:
        print(f"Resultado: {precedencia(operador=opera)}")
    else:
        print("Resultado: -1")
if __name__=="__main__":
    main()

