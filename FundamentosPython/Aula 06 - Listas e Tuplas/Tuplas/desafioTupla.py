# Crie uma tupla contendo os números de 0 a 15 escritos por extenso. Em seguida, solicite ao usuário que digite um número inteiro dentro desse intervalo e exiba o número informado por extenso.

tuplas = ("ZERO" , "UM" , "DOIS" , "TRÊS" , "QUATRO" , "CINCO" , "SEIS" , "SETE" , "OITO" , "NOVE" , "DEZ" , "ONZE" , "DOZE" , "TREZE" , "QUATORZE" , "QUINZE")

numero = int(input("Digite um número: "))

print(tuplas[numero])