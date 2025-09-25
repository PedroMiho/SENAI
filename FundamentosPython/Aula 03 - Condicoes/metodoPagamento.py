# Valor gasto pelo usuario.
# Metodo de pagamento
#   - Dinheiro/Pix = 10% desconto
#   - Credito = Valor total  

valorGasto = int(input("Informe o valor gasto: "))
print("INFORME O MÉTODO DE PAGAMENTO")
print("1 - DINHEIRO/PIX")
print("2 - CRÉDITO")
metodoPagamento = input("Digite o método de pagamento: ")

if metodoPagamento == "1":   
    valorFinal = valorGasto * 0.9
    print(f"O valor a ser pago é de R$ {valorFinal}")
else :
    print(f"O valor a ser pago é de R$ {valorGasto}")
    