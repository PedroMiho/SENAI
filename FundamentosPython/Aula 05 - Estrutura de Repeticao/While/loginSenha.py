loginSalvo = "admin"
senhaSalva = "admin"

tentativas = 4

while True: 
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    if login == loginSalvo and senha == senhaSalva:
        print("Acesso liberado")
        break
    elif tentativas <= 0:
        print("Acesso bloqueado")
        break
    else:
        print("Acesso negado, tente novamente")
        tentativas = tentativas - 1
        
        
    