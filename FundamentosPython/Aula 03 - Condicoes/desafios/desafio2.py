# Desafio 02
# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem cobrando R$
# 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
# viagens mais longas.

distanciaViagem = int(input("Digite a distancia da sua viagem: "))

if distanciaViagem > 200:
    valorTotal = distanciaViagem * 0.45
    print(f"Valor a ser pago será de R$ {valorTotal}")
else:
    valorTotal = distanciaViagem * 0.5
    print(f"Valor a ser pago será de R$ {valorTotal}")