# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

# Considere o dólar = R$ 5,00

dinheiro = int(input("Digite quantos reais você possui: "))

dolar = 5
conversao = dinheiro / dolar

print(f"Com R$ {dinheiro} você pode comprar US${conversao}")