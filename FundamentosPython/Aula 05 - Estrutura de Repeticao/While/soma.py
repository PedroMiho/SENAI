#Crie um programa que some todos os valores digitados pelo usuario.

soma = 0

while True:
    numero = int(input("Digite um número: "))
    
    soma = soma + numero
    
    continuar = input("Deseja continuar [S/N]: ").upper()
    print(soma)
    
    if continuar == "N":
        break

    