listaLanches = ["X-Burguer","X-Bacon","Hot-Dog","X-Salada","X-Tudo"]
listaPreco = [30.00, 35.00, 25.00, 32.50, 40.00]
listaLanchesUsuario = []
listaPrecoUsuario = []

print("BEM-VINDO A LANCHONETE SENAI")

while True:

    i = 1
    for lanche, preco in zip(listaLanches, listaPreco):
        print(f"{i} - {lanche} - R$ {preco}")
        i = i + 1
    print(f"{i} - Para sair")
    
    posicao = int(input("Digite a posição do lanche que deseja: ")) - 1
    
    if posicao == 5:
        print("FIM")
        break
    else:
        listaLanchesUsuario.append(listaLanches[posicao])    
        listaPrecoUsuario.append(listaPreco[posicao])   

print("O SEU PEDIDO FOI")
for lanches, preco in zip(listaLanchesUsuario, listaPrecoUsuario):
    print(f"{lanches} - R$ {preco}")

print(f"O valor final foi de R$ {sum(listaPrecoUsuario)}")