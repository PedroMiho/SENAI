#Identificar todos os numeros pares de 0 a 100
#Somar todos esse numero

soma = 0
for i in range (0, 101):
    
    resto = i % 2
    
    if resto == 0:
        print(i)
        soma = soma + i

print(soma)