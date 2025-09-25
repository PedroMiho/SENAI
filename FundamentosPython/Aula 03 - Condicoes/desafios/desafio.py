# Desafio 01
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = int(input("Digite a sua velocidade: "))

if velocidade > 80:
    velocidadeUltrapassada = velocidade - 80
    multa = velocidadeUltrapassada * 7
    print(f"A velocidade ultrapassada foi de {velocidadeUltrapassada} e o valor da multa é de R$ {multa}")
else:
    print('Você anda conforme as leis de trânsito')