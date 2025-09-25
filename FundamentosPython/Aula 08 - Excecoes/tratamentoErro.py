while True:
    try:
        numero = int(input("Digite um número: "))
        numero2 = int(input("Digite um número: "))
        divisao = numero / numero2
        print(divisao) 
        break
    except (ValueError):
        print("Você digitou uma letra")
    except (ZeroDivisionError):
        print("Informe um divisor diferente de 0")

print("FIM")