import random

maquina = random.randint(0 , 10)
creditos = 3

while True:
    
    if creditos <= 0:
        creditos = int(input("Digite quantos creditos você deseja comprar ou  0 para sair: "))
    else:
        usuario = int(input("Digite um número: "))

    if usuario == maquina :
        print(f"Você venceu, o número gerado foi {maquina}")
        break
    elif creditos <= 0 :
        print(f"Acabaram seus creditos")
        break   
    else:
        print("Tente Novamente")
        creditos = creditos - 1
        