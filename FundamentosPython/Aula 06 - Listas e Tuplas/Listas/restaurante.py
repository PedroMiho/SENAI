listaLanches = ["X-Burguer","X-Bacon","Hot-Dog","X-Salada","X-Tudo"]
listaPreco = [30.00, 35.00, 25.00, 32.50, 40.00]

i = 1
print("BEM-VINDO A LANCHONETE SENAI")
for lanche, preco in zip(listaLanches, listaPreco):
    print(f"{i} - {lanche} - R$ {preco}")
    i = i + 1
    
posicao = int(input("Digite a posição do lanche que deseja: ")) - 1

print(f"O lanche pedido foi {listaLanches[posicao]} e o total foi R$ {listaPreco[posicao]}")