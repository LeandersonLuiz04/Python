precos_originais = [4.95, 9.95, 14.95, 19.95, 24.95]

desconto_percentual = 60

print("Preço Original   |   Desconto   |   Preço com Desconto")
print("----------------------------------------------------")

for preco_original in precos_originais:
    
    desconto = preco_original * (desconto_percentual / 100)
    
    preco_com_desconto = preco_original - desconto
    

    print(f"R$ {preco_original:.2f}           |   R$ {desconto:.2f}   |   R$ {preco_com_desconto:.2f}")

