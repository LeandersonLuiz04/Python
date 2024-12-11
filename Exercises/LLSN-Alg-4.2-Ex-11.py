logo='''

┌─┐┌─┐┬  ┬┌┐┌┌┬┐┬─┐┌─┐┌┬┐┌─┐
├─┘├─┤│  ││││ ││├┬┘│ │││││ │
┴  ┴ ┴┴─┘┴┘└┘─┴┘┴└─└─┘┴ ┴└─┘

'''
print(logo)

while True:
    frase=input('Digite uma frase: ').lower()    
    
    if frase =="":
        break
    
    frase.replace(" ","")
    frase_sem_espaçamento=frase[::-1]    
    
    if frase_sem_espaçamento==frase[::-1]:
        print(f"A frase '{frase}' é um palíndromo. ")
    else:
        print(f"A frase '{frase}' não é um palíndromo. ")

