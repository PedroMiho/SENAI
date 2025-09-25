# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0

for i in range (0, 501):
    resto3 = i % 3
    resto2 = i % 2 
    
    if resto3 == 0 and resto2 == 1:
        soma = soma + i

print(f"A soma final foi de : {soma} ")