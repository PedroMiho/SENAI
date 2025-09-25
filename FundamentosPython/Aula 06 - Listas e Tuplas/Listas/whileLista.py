listaNumero = []

while True:
    
    numero = int(input("Digite um número ou 999 para parar: "))
    
    if numero == 999:
        print("FIM")
        break
    
    listaNumero.append(numero)
    
    for num in listaNumero:
        print(num)