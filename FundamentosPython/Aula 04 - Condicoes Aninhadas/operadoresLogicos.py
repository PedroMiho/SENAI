#Cadastro Usuario
loginSalvo = "admin"
senhaSalva = "admin"

#Acessar a conta
login = input("Digite o seu login: ")
senha = input("Digite a sua senha: ")

if login == loginSalvo and senha == senhaSalva:
    print("Acesso Liberado")
else:
    print("Acesso Negado")
    
#Crie um programa que verifique se um aluno foi aprovado.
#Para o aluno ser aprovado ele deve ter:
# Média >= 70
# Frequência >= 75

n1 = int(input("Digite uma nota: "))
n2 = int(input("Digite uma nota: "))
frequencia = int(input("Digite a sua frequência: "))


media = (n1 + n2) / 2

if media >= 70 and frequencia >= 75:
    print("Aprovado")
else :
    print("Reprovado")
    