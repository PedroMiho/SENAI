# Crie um programa que leia nome, idade e
# carteira de trabalho e cadastre-os em um
# dicionário se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o tempo de contribuição e o salário.

# Calcule e acrescente, além da idade, com quantos anos a
# pessoa vai se aposentar.

# Sabendo que ele vai se aposentar após 35 anos de
# colaboração.

colaborador = {
    "nome" : input("Digite seu nome: "),
    "idade" : int(input("Digite sua idade: ")),
    "CTPS" : int(input("Digite sua CTPS: "))
}

if colaborador["CTPS"] != 0:
    colaborador["contribuicao"] = int(input("Digite o tempo de contribuição: "))
    colaborador["salario"] = int(input("Digite seu salario: "))
    restante = 35 - colaborador["contribuicao"]
    sonho = colaborador["idade"] + restante
    colaborador["Sonho"] = sonho


for chave, valor in colaborador.items():
    print(f"{chave} - {valor}")
