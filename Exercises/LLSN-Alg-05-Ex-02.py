def imprime_n_vezes(nome,n):
    contador=0
    while contador!=n:
        print(nome)
        contador+=1
msg=input("MENSAGEM: ")
numero=int(input("NÚMERO DE REPETIÇÃO: "))
result=imprime_n_vezes(msg,numero)