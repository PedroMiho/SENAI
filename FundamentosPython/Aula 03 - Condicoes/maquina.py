import random

maquina = random.randint(0 , 5)
usuario = int(input("Digite um número: "))

if usuario == maquina:
    print("Você acertou")
else:
    print("Você errou")

print(f"O número aleatório era {maquina}")