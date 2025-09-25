def texto():
    print("Olá, Mundo")
    print("Hello World")

valorTotal = 10

def decrementa():
    global valorTotal
    valorTotal = valorTotal - 1

def incrementa():
    global valorTotal
    valorTotal = valorTotal + 1

decrementa()
decrementa()
decrementa()
incrementa()

def soma():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    soma = n1 + n2
    print(soma)

def subtracao ():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    subtracao = n1 - n2
    return subtracao

#print(subtracao() + 1)
#print(soma() + 1)

soma()
print(subtracao())