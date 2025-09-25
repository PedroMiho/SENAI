estado = {}

while True:
    estadoUsuario = input("Digite seu estado: ")
    ufUsuario = input("Digite a sua UF: ")
    estado[estadoUsuario] = ufUsuario
    continuar = input("Deseja continuar [S/N]: ").upper()
    if continuar == "N":
        break

for chave, valor in estado.items():
    print(f"{chave} - {valor}")
