def potencia(x,y):
    result = 1
    for _ in range(y):
        result *= x
    return result


valor_x=int(input("VALOR DE X: "))
valor_y=int(input("VALOR DE Y: "))
print(potencia(x=valor_x,y=valor_y))