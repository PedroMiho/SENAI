# listas = []
# tuplas = ()
# dicionarios = {}

lanchonete = {
    "X-Buguer" : 30,
    "X-Bacon" : 34,
    "Hot-Dog" : 25,
    "X-Salada" : 32.50,
    "X-Tudo" : 40   
}

print(lanchonete)

#Adicionar itens no dicionario
lanchonete["X-Egg"] = 32.50
print(lanchonete)

#Alterar valores do dicionario
lanchonete["Hot-Dog"] = 27.50
print(lanchonete)

#Remover o item do dicionario
del lanchonete["X-Egg"]
print(lanchonete)

#Mostrar os itens de um dicionario
print(lanchonete.items())

#Mostrar os valores do dicionario
print(lanchonete.values())

#Mostrar as chaves do dicionario
print(lanchonete.keys())

#Percorrer um dicionario
print("LANCHONETE SENAI")
for chave, valor in lanchonete.items():
    print(f"{chave} - R$ {valor}")
    
#Percorrer um dicionario
print("LANCHONETE SENAI")
for posicao, (chave, valor) in enumerate(lanchonete.items()):
    print(f"{posicao} - {chave} - R$ {valor}")