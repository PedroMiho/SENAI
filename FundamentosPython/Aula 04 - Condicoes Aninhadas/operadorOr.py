# Uma pessoa deseja ir ao cinema e pagar meia-entrada. Para pagar meia, ela pode ser menor de 10 anos ou estudante. Crie um programa que pergunte a idade da pessoa e se ela é estudante, e informe se ela pode pagar meia-entrada.

idade = int(input("Digite a sua idade: "))
estudante = input("Você é estudante [S/N]: ").upper()

if idade <= 10 or estudante == "S":
    print("Você pagará meia-entrada")
else: 
    print("Você pagará a entrada cheia")

#Desenvolva um sistema que monitora a temperatura de um equipamento.
# Se a temperatura estiver abaixo de 5°C ou acima de 45°C, deve ser emitido um alerta de risco.
    
temperatura = int(input("Digite a temperatura: "))

if temperatura < 5 or temperatura > 45:
    print("Alerta, temperatura irregular")
else:
    print("Temperatura Estável")