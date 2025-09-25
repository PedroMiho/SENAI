estado = {}
brasil = []

while True:
    #Criando a chave UF
    estado["UF"] = input("Digite sua UF: ")
    #Criando a chave Estado
    estado["Estado"] = input("Digite seu estado: ")
    #Salvando o Dicionario na Lista
    brasil.append(estado.copy())
    print(brasil)
    continuar = input("Deseja continuar [S/N]: ").upper()
    if continuar == "N":
        break


for dicionario in brasil:
    for chave, valor in dicionario.items():
        print(f"{chave} - {valor}")