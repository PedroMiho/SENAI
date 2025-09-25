listaTimes = ["Santos", "São Paulo", "Corinthians", "Palmeiras"]

print(listaTimes)

#Acessando os itens na lista
print(listaTimes[0])
print(listaTimes[1])
print(listaTimes[2])
print(listaTimes[3])

#Adicionar itens na lista
listaTimes.append("Flamengo")
listaTimes.append("Vasco")
print(listaTimes)

#Adiocionar itens na lista em um posição desejada
listaTimes.insert(3, "Botafogo")
listaTimes.insert(2, "Fluminense")
print(listaTimes)

#Alterar itens 
listaTimes[3] = "Internacional"
print(listaTimes)

#Ordenar os itens
print(sorted(listaTimes))

#Identificar o tamanho da lista
print(len(listaTimes))

#Posição de um elemento
print(listaTimes.index("Palmeiras"))

#Contar quantidade de vezes que um item aparece
print(listaTimes.count("Santos"))

#Inverter a ordem da lista
print(sorted(listaTimes, reverse = True))

#Excluir um item
listaTimes.remove("Flamengo")
print(listaTimes)

#Excluir o ultimo item
listaTimes.pop()
print(listaTimes)

#Copiando uma lista
brasileirao = listaTimes.copy()
print(brasileirao)

#Percorrer a lista
for times in listaTimes:
    print(times)

print("MAIORES TIMES DO BRASIL")
for numero, times in enumerate(listaTimes):
    print(f"{numero+1} - {times}")