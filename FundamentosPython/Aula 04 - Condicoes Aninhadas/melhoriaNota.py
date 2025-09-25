n1 = int(input("Digite a sua nota: "))
n2 = int(input("Digite a sua nota: "))

media = (n1 + n2) / 2
print(f"A média foi de {media}")

if media >= 70:
    print("Aprovado")
elif media >= 50:
    print("Recuperação")
    n3 = int(input("Digite a sua nota na recuperação: "))
    mediaFinal = (media + n3) / 2
    
    print(f"A média foi de {mediaFinal}")
    if mediaFinal >= 70:
        print("Aprovado") 
    else:
        print("Reprovado")
else:
    print("Reprovado")

