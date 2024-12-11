
logo='''

'  ┌┬┐┌─┐┌─┐┬┌┬┐┌─┐┬    ┌─┐┌─┐┬─┐┌─┐  ┌┐ ┬┌┐┌┌─┐┬─┐┬┌─┐
'   ││├┤ │  ││││├─┤│    ├─┘├─┤├┬┘├─┤  ├┴┐││││├─┤├┬┘││ │
'  ─┴┘└─┘└─┘┴┴ ┴┴ ┴┴─┘  ┴  ┴ ┴┴└─┴ ┴  └─┘┴┘└┘┴ ┴┴└─┴└─┘


'''
print(logo)
def binario_decimal(n_decimal):
    if n_decimal==0:
        return "0"
    result=""
    q=n_decimal
    while q!=0:
        r=q%2
        result=str(r)+result
        q//=2
    return result


n_decimal=int(input("Digite aqui o número decimal: "))
x=binario_decimal(n_decimal)

print(f"EM BINÁRIO: {x}")


