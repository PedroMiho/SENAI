# import math

# def circulo (raio):
#     area = math.pi * raio ** 2
#     perimetro = 2 * math.pi * raio
#     print(f"Área {area:.2f}")
#     print(f"Perímetro {perimetro:.2f}")

# circulo(5)

# def retangulo (largura, altura):
#     area = largura * altura
#     perimetro = 2 * largura + 2 * altura
#     print(f"Área {area:.2f}")
#     print(f"Perímetro {perimetro:.2f}")

# altura = int(input("Digite a altura: "))
# largura = int(input("Digite a largura: "))

# retangulo(largura, altura)
 
import math


def triangulo (base, altura, ladoB=0, ladoC=0 ):
    
    #Equilátero
    if ladoB == 0 and ladoC == 0:
        perimetro = base * 3
        area = base * altura / 2
    #Isósceles   
    elif ladoC == 0:
        perimetro = base + ladoB + ladoB
        area = base * altura / 2
    #Escaleno
    else :
        perimetro = base + ladoB + ladoC
        area = base * altura / 2
        
    print(f"Área {area:.2f}")
    print(f"Perímetro {perimetro:.2f}")

triangulo(10,10)
triangulo(10,10,5)
triangulo(10,10,5,3)

#Hexagono

def hexagono(lado):
    perimetro = 6 * lado
    area = (6 * lado ** 2 * math.sqrt(3)) / 4
    print(f"Área {area:.2f}")
    print(f"Perímetro {perimetro:.2f}")

hexagono(6)