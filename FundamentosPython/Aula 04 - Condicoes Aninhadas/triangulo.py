# Desenvolva um programa em Python que solicite três valores inteiros representando os lados de um triângulo, e informe se o triângulo é 

# Equilátero (todos os lados iguais)
# Isósceles (dois lados iguais) 
# Escaleno (todos diferentes).


ladoA = int(input("Digite um lado: ")) 
laboB = int(input("Digite um lado: "))
ladoC = int(input("Digite um lado: "))

if ladoA == laboB and ladoA == ladoC  and laboB == ladoC:
    print("TRIÂNGULO EQUILÁTERO")
elif ladoA == laboB or ladoA == ladoC or ladoC == laboB:  
    print("TRIÂNGULO ISÓCELES")
elif ladoA != laboB and ladoA != ladoC and laboB != ladoC:
    print("TRIÂNGULO ESCALENO")
    