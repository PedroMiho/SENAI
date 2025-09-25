# Valor gasto pelo usuario.
# Metodo de pagamento
#   - Dinheiro/Pix = 10% de desconto
#   - Debito = 5% de desconto
#   - Credito
#       - A vista = Valor total
#       - 2x = 5% de acrescimo - Valor de cada parcela
#       - 3x = 10% de acrescimo - Valor de cada parcela

valorGasto = int(input("Informe o valor gasto: "))
print("INFORME O MÉTODO DE PAGAMENTO")
print("1 - DINHEIRO/PIX")
print("2 - DEBITO")
print("3 - CRÉDITO")
metodoPagamento = input("Digite o método de pagamento: ")

if metodoPagamento == "1":   
    valorFinal = valorGasto * 0.9
    print(f"O valor a ser pago é de R$ {valorFinal}")
elif metodoPagamento == "2":
    valorFinal = valorGasto * 0.95
    print(f"O valor a ser pago é de R$ {valorFinal}")
else :
    print("MÉTODO DE PARCELAMENTO")
    print("1 - A vista")
    print("2 - 2x c/ juros de 5%")
    print("3 - 3x c/ juros de 10%")
    metodoParcelamento = input("Digite o metodo de parcelamento: ")
    
    if metodoParcelamento == "1":
        print(f"O valor a ser pago é de R$ {valorGasto}")
    elif metodoParcelamento == "2":
        valorFinal = valorGasto * 1.05
        valorParcela = valorFinal / 2
        print(f"O valor a ser pago é de R$ {valorFinal:.2f}")
        print(f"E o valor de cada parcela vai ser de R$ {valorParcela:.2f}")
    else:
        valorFinal = valorGasto * 1.1
        valorParcela = valorFinal / 3
        print(f"O valor a ser pago é de R$ {valorFinal:.2f}")
        print(f"E o valor de cada parcela vai ser de R$ {valorParcela:.2f}")    
    
    
    